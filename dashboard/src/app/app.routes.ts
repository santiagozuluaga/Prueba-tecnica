import { Routes } from '@angular/router';

import { DocumentsComponent } from '@/views/documents/documents.component';
import { CreateDocumentComponent } from '@/views/create-document/create-document.component';
import { DocumentComponent } from '@/views/document/document.component';

export const routes: Routes = [
    {path: '', redirectTo: '/documents', pathMatch: 'full'},
    {path: 'documents', component: DocumentsComponent},
    {path: 'documents/create', component: CreateDocumentComponent},
    {path: 'documents/:documentId', component: DocumentComponent},
];
