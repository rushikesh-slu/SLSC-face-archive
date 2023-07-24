import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { ImageUploadComponent } from './image-upload/image-upload.component';
import { HomeComponent } from './home/home.component';
import { PersonGalleryComponent } from './person-gallery/person-gallery.component';

@NgModule({
  declarations: [
    AppComponent,
    ImageUploadComponent,
    HomeComponent,
    PersonGalleryComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
