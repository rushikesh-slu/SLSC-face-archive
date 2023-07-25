import { Injectable } from '@angular/core';
import { HttpClient} from "@angular/common/http";
import { environment } from 'src/environments/environment';
@Injectable({
  providedIn: 'root'
})
export class ApiService {

  API_ENDPOINT = environment.API_ENDPOINT;
  constructor(private http: HttpClient) { }
  
  // sendOTP(payload){
  //   return this.http.post(`${this.API_ENDPOINT}/api/user/sendotp`,payload)
  // }
  getPersons(){
    return this.http.get(`${this.API_ENDPOINT}/api/user/getall`)
  }
  getallPhotos(payload){
    return this.http.post(`${this.API_ENDPOINT}/api/user/getperson`,payload)
  }
}
