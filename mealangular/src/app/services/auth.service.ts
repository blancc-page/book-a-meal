import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { HttpHeaders } from '@angular/common/http';
import { map } from 'rxjs';
import { Observable } from 'rxjs';

const httpOptions = {
  headers: new HttpHeaders({
    'Content-Type': 'application/json'
  })
};

@Injectable({
  providedIn: 'root'
})
export class AuthService {
  api_url: string = 'http://127.0.0.1:8000/';

  constructor(private http: HttpClient) { }

  loginUser(email: string, password: string):Observable<any>{
    return this.http.post<any>(this.api_url + 'api-auth/', 
    { email, password}, httpOptions).pipe(
      map(user => {
        if (user) {
          localStorage.setItem("currentUser", JSON.stringify(user));
        }
        return user;
      })
    );
  }
  register(username: string, email: string, password: string): Observable<any> {
    return this.http.post(this.api_url + 'api-auth/', {
      username,
      email,
      password
    }, httpOptions);
  }
  logout(){
    localStorage.removeItem('currentUser');
  }
}
