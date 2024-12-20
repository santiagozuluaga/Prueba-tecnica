import { Component, inject } from '@angular/core';
import { Router, RouterLink } from '@angular/router';
import {FormBuilder, Validators, FormsModule, ReactiveFormsModule, FormArray} from '@angular/forms';
import { MatIconModule } from '@angular/material/icon';
import { MatButtonModule } from '@angular/material/button';
import { MatSnackBar } from '@angular/material/snack-bar';
import { MatInputModule } from '@angular/material/input';
import { MatFormFieldModule } from '@angular/material/form-field';
import {MatStepperModule} from '@angular/material/stepper';
import { DocumentsService } from '@/services/documents.service';
import { FormDocumentComponent } from "@/components/form-document/form-document.component";

@Component({
  selector: 'app-create-document',
  imports: [
    RouterLink,
    MatIconModule,
    MatButtonModule,
    MatInputModule,
    MatFormFieldModule,
    MatStepperModule,
    FormsModule,
    ReactiveFormsModule,
    FormDocumentComponent
],
  templateUrl: './create-document.component.html',
  styleUrl: './create-document.component.css'
})
export class CreateDocumentComponent {
  action: string = "create";
  isLinear: boolean = true;
  isCreatingDocument: boolean = true;

  private router = inject(Router);
  private snackBar = inject(MatSnackBar);
  private documentsService = inject(DocumentsService);

  submit(formData: any): void {
    const { documentData, signersData } = formData

    this.isCreatingDocument = true;
    this.documentsService
      .createDocument({
        name: documentData.documentName,
        url_pdf: documentData.documentURL,
        signers: signersData.map((signer: any) => {
          return {
            name: signer.signerName,
            email: signer.signerEmail,
            external_id: signer.signerExternalId,
          }
        }),
        external_id: documentData.documentExternalId,
      })
      .subscribe({
        next: (response) => {
          this.isCreatingDocument = false;
          this.snackBar.open(
            "Document created successfully.",
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
          this.isCreatingDocument = false;
          this.snackBar.open(err.error.message, "Close")
        }
      });
  };
}
