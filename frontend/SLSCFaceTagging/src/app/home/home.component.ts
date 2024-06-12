import { Component } from '@angular/core';
import { ApiService } from '../services/api/api.service';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent {

  constructor (private api: ApiService) {}
  images: any[] = [];
  ngOnInit(): void {
    this.api.getPersons().subscribe(result =>{
      let res = result["unique"]
      for(var img of res){
        let tempStr = 'assets/result/'+img["person"]+"/"+img["icon"]
        let temp = {
          url: tempStr,
          name : img["name"],
          id : img["person"]
        }
        this.images.push(temp)
      }
    })

    
  }
  
}