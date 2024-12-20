import { Component, EventEmitter, inject, Input, Output } from '@angular/core';
import { FormArray, FormBuilder, FormsModule, ReactiveFormsModule, Validators } from '@angular/forms';
import { MatButtonModule } from '@angular/material/button';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatInputModule } from '@angular/material/input';
import { MatStepperModule } from '@angular/material/stepper';

@Component({
  selector: 'app-form-document',
  imports: [
    MatButtonModule,
    MatInputModule,
    MatFormFieldModule,
    MatStepperModule,
    FormsModule,
    ReactiveFormsModule,
  ],
  templateUrl: './form-document.component.html',
  styleUrl: './form-document.component.css'
})
export class FormDocumentComponent {
  @Input() action!: string;
  @Input() documentData: any;
  @Input() signersData: any[] = [];
  @Output() submitForm = new EventEmitter<any>();

  isLinear: boolean = true;

  private formBuilder = inject(FormBuilder);

  documentGroup = this.formBuilder.group({
    documentURL: ['', this.action === "create" && Validators.required],
    documentName: ['', Validators.required],
    documentExternalId: [''],
  });
  signersGroup = this.formBuilder.group({
    signers: this.formBuilder.array(
      [
        this.formBuilder.group({
          signerId: [''],
          signerName: ['', Validators.required],
          signerEmail: ['', [Validators.required, Validators.email]],
          signerExternalId: [''],
        }),
      ],
      [
        Validators.required,
        Validators.minLength(1),
        Validators.maxLength(3),
      ]
    ),
  });

  get signers(): FormArray {
    return this.signersGroup.get('signers') as FormArray;
  }

  addSigner() {
    this.signers.push(
      this.formBuilder.group({
        signerId: [''],
        signerName: ['', Validators.required],
        signerEmail: ['', [Validators.required, Validators.email]],
        signerExternalId: [''],
      })
    );
  };

  removeSigner(index: number) {
    this.signers.removeAt(index)
  }

  submit(): void {
    const documentData = this.documentGroup.value;
    const signersData = this.signers.value;

    // Emitir los datos al componente padre para su manejo
    this.submitForm.emit({
      documentData,
      signersData,
    });
  }

  ngOnInit(): void {
    console.log(this.action)
    if (!this.documentData || !this.signersData) {
      return
    }

    this.documentGroup.patchValue({
      documentURL: this.documentData.documentURL,
      documentName: this.documentData.documentName,
      documentExternalId: this.documentData.documentExternalId,
    });

    const signersArray = this.formBuilder.array(
      this.signersData.map(signer => this.formBuilder.group({
        signerId: [signer.signerId, Validators.required],
        signerName: [signer.signerName, Validators.required],
        signerEmail: [signer.signerEmail, [Validators.required, Validators.email]],
        signerExternalId: [signer.signerExternalId],
      }))
    );
    this.signersGroup.setControl('signers', signersArray);
  }
}
