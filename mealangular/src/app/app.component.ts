import { Component } from '@angular/core';
import { PublicService } from './services/public.service';

declare var fixNav: any

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'Book A Meal - The World\'s Best Food Delivery Site!';
  msg: any;
  constructor (private pService: PublicService) {

  }
  ngOnInit(): void {
    this.showMessage();
    new fixNav();
  }
  showMessage() {
  this.pService.getMessage().subscribe(data=>{
    this.msg = data,
    console.log(this.msg);
  });
  }
}
