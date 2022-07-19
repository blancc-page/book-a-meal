import { Component, OnInit } from '@angular/core';
import { catchError, throwError } from 'rxjs';
import { CartService } from 'src/app/services/cart.service';
import { PublicService } from 'src/app/services/public.service';

@Component({
  selector: 'app-order',
  templateUrl: './order.component.html',
  styleUrls: ['./order.component.css']
})
export class OrderComponent implements OnInit {

  items: any[] = [];
  totalPrice: number = 0;

  constructor(private cartService: CartService, private publicService: PublicService) { }

  ngOnInit(): void {
    this.items = this.cartService.getItems();
    this.totalPrice = this.gettotalPrice();
  }
  
  gettotalPrice(): number{
    // let totalPrice = 0;
    this.items.forEach(item => {
      // console.log(item[1])
        this.totalPrice += Number(item[1]);
    });
    console.log(this.totalPrice);
    return this.totalPrice;

}

handleError(error: any) {
  alert(error.error[Object.keys(error.error)[0]]);
  return throwError(error);
}

addOrders(){
  let items = this.cartService.getItems();

  items.map(item => {
    this.publicService.addOrder(item[0]).pipe(
      catchError(this.handleError)
    ).subscribe(
      data=>{
        console.log(data);
      }
    )

  })
  alert("Your order(s) have been placed!")
  window.location.href = "/"
}

}


