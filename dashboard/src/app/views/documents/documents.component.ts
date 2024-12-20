import { Component, inject } from '@angular/core';
import { RouterLink } from '@angular/router';
import { MatSnackBar } from '@angular/material/snack-bar';
import { MatButtonModule } from '@angular/material/button';
import { MatTableModule } from '@angular/material/table';
import { DocumentsService } from '@/services/documents.service';

import { formatDate } from '@/utils/date';

@Component({
  selector: 'app-documents',
  imports: [
    RouterLink,
    MatButtonModule,
    MatTableModule,
  ],
  templateUrl: './documents.component.html',
  styleUrl: './documents.component.css'
})
export class DocumentsComponent {
  private snackBar = inject(MatSnackBar);
  private documentsService = inject(DocumentsService);

  documents: any[] = [];
  isFetchingDocuments: boolean = true;
  isDeletingDocument: boolean = false;
  displayedColumns: string[] = ['id', 'name', 'status', 'signers', 'created_at', 'actions'];

  ngOnInit(): void {
    this.getDocuments();
  };

  getDocuments(): void {
    this.isFetchingDocuments = true;
    this.documentsService
      .getDocuments()
      .subscribe({
        next: (response) => {
          this.documents = response.documents
          this.isFetchingDocuments = false;
        },
        error: (err) => {
          this.isFetchingDocuments = false;
          this.snackBar.open(err.error.message, "Close")
        }
      });
  }

  deleteDocument(documentId: number): void {
    if (!documentId) {
      return
    }
    this.isDeletingDocument = true;
    this.documentsService
      .deleteDocument(documentId)
      .subscribe({
        next: (response) => {
          this.isDeletingDocument = false;
          this.snackBar.open(
            response.message,
            "Close"
          )
          this.getDocuments();
        },
        error: (err) => {
          this.isDeletingDocument = false;
          this.snackBar.open(err.error.message, "Close")
        }
      });
  };

  formatDocumentDate(createdAt: string) {
    return formatDate(createdAt);
  };
}
