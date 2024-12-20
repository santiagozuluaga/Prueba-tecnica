import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class DocumentsService {
  constructor(private http: HttpClient) {}

  createDocument(data: any): Observable<any> {
    return this.http.post<any>(`${import.meta.env.NG_APP_BASE_API_URL}/docs/`, data);
  }

  updateDocument(documentId: number, data: any): Observable<any> {
    return this.http.put<any>(`${import.meta.env.NG_APP_BASE_API_URL}/docs/${documentId}/`, data);
  }

  getDocuments(): Observable<any> {
    return this.http.get<any>(`${import.meta.env.NG_APP_BASE_API_URL}/docs/`);
  }

  getDocument(documentId: number): Observable<any> {
    return this.http.get<any>(`${import.meta.env.NG_APP_BASE_API_URL}/docs/${documentId}/`);
  }

  deleteDocument(documentId: number): Observable<any> {
    return this.http.delete<any>(`${import.meta.env.NG_APP_BASE_API_URL}/docs/${documentId}/`);
  }
}
