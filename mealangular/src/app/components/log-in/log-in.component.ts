import { Component, OnInit } from '@angular/core';
import { FormControl, FormGroup } from '@angular/forms'; 
import { first } from 'rxjs';
import { AuthService } from 'src/app/services/auth.service';

@Component({
  selector: 'app-log-in',
  templateUrl: './log-in.component.html',
  styleUrls: ['./log-in.component.css']
})
export class LogInComponent implements OnInit {
  
  myForm!: FormGroup;

  constructor(private authService: AuthService) { }

  ngOnInit(): void {
    this.myForm = new FormGroup({
      email: new FormControl(''),
      password: new FormControl('')
    })
  }

  get f(){
    return this.myForm.controls;
  }
  onSubmit() {
    this.authService.loginUser(this.f['email'].value, this.f['password'].value).pipe(first()).subscribe(
      data => {
        console.log(data);
      }
      
    )
    
  }

}
