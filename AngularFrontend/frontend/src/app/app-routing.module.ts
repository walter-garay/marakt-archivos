import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { PrincipalComponent } from './principal/principal.component';
import { BusquedaComponent } from './busqueda/busqueda.component';
import { RegistroComponent } from './registro/registro.component';

const routes: Routes = [
  {path:'principal',component:PrincipalComponent},
  {path:'busqueda',component:BusquedaComponent},
  {path:'registro',component:RegistroComponent},
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
