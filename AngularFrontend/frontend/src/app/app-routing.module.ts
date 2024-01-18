import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { PrincipalComponent } from './principal/principal.component';
import { BusquedaComponent } from './busqueda/busqueda.component';

const routes: Routes = [
  {path:'principal',component:PrincipalComponent},
  {path:'busqueda',component:BusquedaComponent},
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
