import { Component, OnInit } from '@angular/core';
import { FormGroup } from '@angular/forms';
import { AuthService } from 'src/app/services/auth.service';

@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.css']
})
export class RegisterComponent implements OnInit {

  is_caterer : any;
  is_customer: any;
  isSuccessful = false;
  isSignUpFailed = false;
  errorMessage = ""
  form: any = {
    username: null,
    email: null,
    password: null
  };




  Roles: any =[
    { name: "Caterer", value: 'caterer' },
    { name: "Customer", value: 'customer' }
  ];
  

  constructor(private authService: AuthService) { }

  ngOnInit(): void {
  }

  changeClient(value: any) {
    if (value.value == 'caterer') {
      this.is_caterer = true;
      this.is_customer = false;
    } else{
      this.is_caterer = false;
      this.is_customer = true;
    }
}
  get f(){
    return this.form.controls;
  }
onSubmit(): void {
  // const data = {
  //   email: this.f['email'].value,
  //   password: this.f['password'].value,
  //   username: this.f['username'].value
  // }
  const { username, email, password } = this.form;
  this.authService.register(username, email, password).subscribe(
    data => {
      console.log(data);
      this.isSuccessful = true;
      this.isSignUpFailed = false;
    },
    err => {
      this.errorMessage = err.error.message;
      this.isSignUpFailed = true;
    }
  );
}

  // createUser(credentials: any){

  //   this.service.createUser(credentials.username, credentials.email, credentials.password, this.is_caterer, this.is_customer).subscribe(
  //     (data: any) => {
  //       console.log(data);
  //     })

  //     window.location.href = '/login';

  //   }

    
}
