import { Component, OnInit } from '@angular/core';
import { FormControl, FormGroup } from '@angular/forms';
import { catchError, throwError } from 'rxjs';
import { Menus } from 'src/app/classes/menus';
import { Order } from 'src/app/classes/order';
import { Menu } from 'src/app/interface/menu';
import { CartService } from 'src/app/services/cart.service';
import { PublicService } from 'src/app/services/public.service';

@Component({
  selector: 'app-menu',
  templateUrl: './menu.component.html',
  styleUrls: ['./menu.component.css']
})
export class MenuComponent implements OnInit {

  form!:FormGroup;
  image!:File;
  name!:string;
  description!:string;
  price!:any;
  items : any[] = [];

  items_count!:number;

  menuArray!: Menus[];

  constructor(private publicservice: PublicService, private cartService: CartService) { }

  ngOnInit(): void {
    this.form = new FormGroup({
      image: new FormControl(''),
      name: new FormControl(''),
      description: new FormControl(''),
      price: new FormControl(''),
    })
  
    this.publicservice.getMenu().then(
      (successful)=>{
        this.menuArray = this.publicservice.menuArray
      },
      (error) => {
        console.log("error")
      }
    )

    this.items = this.cartService.getItems();
    this.items_count = this.cartService.getItemCount()
  
  }
  

  onImageChange(event: any){
    this.image = event.target.files[0]
  }

  onNameChange(event: any){
    this.name = event.target.value
  }

  onDescriptionChange(event: any){
    this.description = event.target.value
  }

  onPriceChange(event: any){
    this.price = event.target.value
  }

  handleError(error: any) {
    alert(error.error[Object.keys(error.error)[0]]);
    return throwError(error);
  }

  onSubmit(){
    const formData = new FormData;
    formData.append('image', this.image, this.image.name)
    formData.append('name', this.name)
    formData.append('description', this.description)
    formData.append('price', this.price)

    this.publicservice.addMenu(formData).pipe(
      catchError(this.handleError)
    ).subscribe(
      data=>{
        console.log(data)
        window.location.reload()
      }
    )
    
  }

  addToCart(menu: any){

    this.cartService.addToCart(menu);
    window.alert("Added to cart!");
    this.items_count = this.cartService.getItemCount()

  
  }


}
