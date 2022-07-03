import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';

const baseUrl = 'http://127.0.0.1:8000/api/v1/users/'

const httpOptions = {
  headers: new HttpHeaders({ 'Content-Type': 'application/json' })
};


@Injectable({
  providedIn: 'root'
})
export class AuthUserService {

  constructor(private http: HttpClient) { }

  loginUser(email: string, password: string) {
    return this.http.post(baseUrl + 'login', { email: email, password: password }, httpOptions);
  }

  createUser(username: string, email: string, password: string, is_caterer: any, is_customer: any) {
    return this.http.post(baseUrl, { username, email, password, is_caterer, is_customer }, httpOptions);
  }

}
