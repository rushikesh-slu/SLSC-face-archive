import { ComponentFixture, TestBed } from '@angular/core/testing';

import { PersonGalleryComponent } from './person-gallery.component';

describe('PersonGalleryComponent', () => {
  let component: PersonGalleryComponent;
  let fixture: ComponentFixture<PersonGalleryComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [PersonGalleryComponent]
    });
    fixture = TestBed.createComponent(PersonGalleryComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
