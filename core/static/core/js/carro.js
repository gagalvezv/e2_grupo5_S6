document.addEventListener('DOMContentLoaded', () => {
    const agregarAlCarrito = document.querySelectorAll('.categorias-link');

    agregarAlCarrito.forEach(btn => {
        btn.addEventListener('click', agregarProducto);
    });

    function agregarProducto(evento) {
        const boton = evento.target;
        const producto = boton.parentElement.parentElement.querySelector('img').src;
        const titulo = boton.parentElement.parentElement.querySelector('h4').textContent;
        const precio = boton.parentElement.parentElement.querySelector('.precio span').textContent;

        agregarAlCarrito(producto, titulo, precio);
    }

    function agregarAlCarrito(producto, titulo, precio) {
        const fila = document.createElement('li');
        fila.innerHTML = `
            <img src="${producto}" alt="">
            <div>
                <h4>${titulo}</h4>
                <p>Precio: ${precio}</p>
            </div>
            <button class="eliminar-item">Eliminar</button>
        `;
        document.querySelector('.lista-carrito').appendChild(fila);
    }

    function actualizarTotal() {
        const listaCarrito = document.querySelector('.lista-carrito');
        const carritoItems = listaCarrito.querySelectorAll('li');

        let total = 0;
        carritoItems.forEach(item => {
            const precio = parseFloat(item.querySelector('.precio span').textContent);
            total += precio;
        });

        document.querySelector('.total').textContent = total.toFixed(2);
    }
});
