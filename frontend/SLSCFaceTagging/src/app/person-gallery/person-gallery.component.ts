import { Component } from '@angular/core';
import { ApiService } from '../services/api/api.service';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-person-gallery',
  templateUrl: './person-gallery.component.html',
  styleUrls: ['./person-gallery.component.css']
})
export class PersonGalleryComponent {

  constructor( private api: ApiService,private route: ActivatedRoute) { }

  images: any[] = [];

  personId :any;

  ngOnInit(): void {

    this.route.params.subscribe(params => {
      this.personId = params['id'];
      console.log(this.personId)
      let payload={
        'id':this.personId
      }
      this.api.getallPhotos(payload).subscribe(result =>{
        let tempImgArray = result["lis"]
        for(var img of tempImgArray){
          let tempStr = 'assets/images/'+img
          let temp = {
            url: tempStr,
          }
          this.images.push(temp)
        }
      })

    });

    
  }
}
