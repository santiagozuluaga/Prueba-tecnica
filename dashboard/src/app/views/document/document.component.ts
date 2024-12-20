import { Component, inject, Input } from '@angular/core';
import { RouterLink, Router } from '@angular/router';
import {MatIconModule} from '@angular/material/icon';
import { MatSnackBar } from '@angular/material/snack-bar';
import { MatButtonModule } from '@angular/material/button';
import { DocumentsService } from '@/services/documents.service';
import { FormDocumentComponent } from "../../components/form-document/form-document.component";

@Component({
  selector: 'app-document',
  imports: [
    RouterLink,
    MatIconModule,
    MatButtonModule,
    FormDocumentComponent
],
  templateUrl: './document.component.html',
  styleUrl: './document.component.css'
})
export class DocumentComponent {
  @Input() documentId!: number;

  action: string = "update";
  isLinear: boolean = true;

  private router = inject(Router);
  private snackBar = inject(MatSnackBar);
  private documentsService = inject(DocumentsService);
  
  documentData: any = {};
  signersData: any[] = [];
  isFetchingDocument: boolean = true;
  isDeletingDocument: boolean = false;
  isUpdatingDocument: boolean = false;

  ngOnInit(): void {
    if (!this.documentId) {
      return
    }
    this.documentsService
      .getDocument(this.documentId)
      .subscribe({
        next: (response) => {
          this.documentData = {
            documentURL: response.url_pdf,
            documentName: response.name,
            documentExternalId: response.external_id,
          }
          this.signersData = response.signers.map((signer: any) => {
            return {
              signerId: signer.id,
              signerName: signer.name,
              signerEmail: signer.email,
              signerExternalId: signer.external_id,
            }
          })
          this.isFetchingDocument = false;
        },
        error: (err) => {
          this.isFetchingDocument = false;
          this.snackBar.open(err.error.message, "Cerrar")
        }
      });
  }

  submit(formData: any): void {
    const { documentData, signersData } = formData

    this.isUpdatingDocument = true;
    this.documentsService
      .updateDocument(this.documentId, {
        name: documentData.documentName,
        signers: signersData.map((signer: any) => {
          return {
            id: signer.signerId,
            name: signer.signerName,
            email: signer.signerEmail,
            external_id: signer.signerExternalId,
          }
        }),
        external_id: documentData.documentExternalId,
      })
      .subscribe({
        next: (response) => {
          this.isUpdatingDocument = false;
          this.snackBar.open(
            response.message,
            "Close"
          )
          setTimeout(
            () => {
              this.router.navigate(['/documents'])
            },
            1000,
          )
        },
        error: (err) => {
          this.isUpdatingDocument = false;
          this.snackBar.open(err.error.message, "Close")
        }
      });
  }
}
