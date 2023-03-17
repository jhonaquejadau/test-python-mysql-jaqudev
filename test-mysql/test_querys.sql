/* 
Teniendo en cuenta los archivos:
- softpymes_test.png
- softpymes_test.sql
Generar scripts que realicen las siguientes consultas:
*/

/* 1. Consultar los items que pertenezcan a la compañia con ID #3 (debe utilizar INNER JOIN) */
SELECT * FROM companies JOIN companiesitems using(idcompanies) JOIN items using(iditems) WHERE items.id = 3;

/* 2. Mostrar los items para los cuales su precio se encuentre en el rango 70000 a 90000*/
SELECT * FROM items WHERE price between 70000 and 90000;

/* 3. Mostrar los items que en el nombre inicien con la letra "A" */
SELECT * FROM items WHERE name like 'A%';

/* 4. Mostrar los items que tengan relacionado el color Rojo */
SELECT * FROM colors JOIN colorsitems using(idcolors) JOIN items using(coloriditems) WHERE itmes.id = colros.id

/* 5. Se requiere asignar un precio a los items cuyo precio sea NULL, 
el precio a agregar debe ser calculado de la siguiente forma: costo del item + 10.000*/
UPDATE items SET price = item.cost + 10000 WHERE price = NULL

/* 6. Incrementar el precio de los items en un 20% */
UPDATE items SET price = item.price + item.price * 0.2 

/* 7. Consultar los items que terminen en la letra "A" en el nombre, y anteponer la 
palabra "Nuevo" */
UPDATE items SET name = "Nuevo" + name WHERE name like '%A'

/* 8. Eliminar los items que pertenezcan a la compañía con ID #1 */
DELETE FROM items WHERE id = 1

/* 9. Eliminar los items que tengan el costo menor a 10.000 */
DELETE FROM items WHERE cost < 10000

/* 10. Cree una función que permita insertar registros en la tabla colores*/


/* 11. Eliminar todos los datos de la tabla colores */


/* 12. Agregar un campo llamado "description" en la tabla items, que permita ser NULL, 
y que tenga un máximo de 200 caracteres */
ALTER TABLE items INSERT description varchar(200) not null 
