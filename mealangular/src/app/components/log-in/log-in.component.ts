import { Component, OnInit } from '@angular/core';
import { FormControl, FormGroup } from '@angular/forms'; 
import { Router } from '@angular/router';
import { first } from 'rxjs';
import { AuthService } from 'src/app/services/auth.service';
import { TokenStorageService } from 'src/app/services/token-storage.service';

@Component({
  selector: 'app-log-in',
  templateUrl: './log-in.component.html',
  styleUrls: ['./log-in.component.css']
})
export class LogInComponent implements OnInit {
  
  myForm!: FormGroup;
  isLoggedIn = false;
  isLoginFailed = false;
  roles: string[]=[];
  errorMessage = " ";

  constructor(private authService: AuthService, private tokenStorage: TokenStorageService, private route: Router) { }

  ngOnInit(): void {
    this.myForm = new FormGroup({
      email: new FormControl(''),
      password: new FormControl('')
    })
    if (this.tokenStorage.getToken()) {
      this.isLoggedIn = true;
      this.roles = this.tokenStorage.getUser().username;
    }
  }



  get f(){
    return this.myForm.controls;
  }
  onSubmit() {
    console.log(this.f['email'].value, this.f['password'].value);
    
    const data = {
      email: this.f['email'].value,
      password: this.f['password'].value
    }
    this.authService.loginUser(this.f['email'].value, this.f['password'].value).pipe(first()).subscribe(
        data => {                
          this.tokenStorage.saveToken(data);
          this.tokenStorage.saveUser(data);
          this.isLoginFailed = false;
          this.isLoggedIn = true;
          this.roles = this.tokenStorage.getUser().username;
          this.route.navigate(['/']);
          this.reloadPage();
        },
        err => {
          this.errorMessage = err.error.message;
          this.isLoginFailed = true;
        }
    )
    console.log("Works!");
  }

  reloadPage(){
    window.location.reload();
  }

}


