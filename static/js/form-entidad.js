$(document).ready(function() {
    $('#select-provincia').change(function() {
        let provincia_id = $(this).val();
        $.ajax({
            url: '/provincias/' + provincia_id + '/cantones/',
            type: 'GET',
            success: function(data) {
                $('#select-canton').empty();
                $('#select-parroquia').empty();
                $.each(data, function(index, canton) {
                    $('#select-canton').append($('<option>', {
                        value: canton.id,
                        text: canton.nombre
                    }));
                });
            },
            error: function(xhr, textStatus, errorThrown) {
                console.error('Error al obtener los cantones:', errorThrown);                
            }
        });
    });

    $('#select-canton').change(function() {
        let canton_id = $(this).val();
        $.ajax({
            url: '/cantones/' + canton_id + '/parroquias/',
            type: 'GET',
            success: function(data) {
                $('#select-parroquia').empty();                
                $.each(data, function(index, parroquia) {
                    $('#select-parroquia').append($('<option>', {
                        value: parroquia.id,
                        text: parroquia.nombre
                    }));
                });
            },
            error: function(xhr, textStatus, errorThrown) {
                console.error('Error al obtener las parroquias:', errorThrown);                
            }
        });
    });

    $('#form-entidad').submit(function(event) {        
        //Evitar que el formulario se envíe de forma convencional.        
        event.preventDefault();
        
        let formEntidad = $(this)[0];

        let formValido = formEntidad.checkValidity()
        formEntidad.classList.add('was-validated');

        if (!formValido) {
            event.stopPropagation();
            return false;
        }

        let csrfToken = $('input[name="csrfmiddlewaretoken"]').val();

        // Obtener los datos del formulario
        let formData = new FormData(formEntidad);

        // Agregar el token CSRF a los datos del formulario
        formData.append('csrfmiddlewaretoken', csrfToken);

        // Enviar los datos al servidor mediante AJAX
        $.ajax({
            url: '/',
            type: 'POST',
            data: formData,
            processData: false,
            contentType: false,
            success: function(response) {
                alert('El registro de la entidad se procesó exitosamente.');
            },
            error: function(xhr, textStatus, errorThrown) {
                console.error('Error al enviar el formulario:', errorThrown);
            
                if (xhr.status === 400 && xhr.responseJSON) {
                    let errores = JSON.parse(xhr.responseJSON.msg_error); // Obtener el JSON de errores de validación
            
                    // Iterar sobre los mensajes de error y agregarlos a los elementos HTML correspondientes
                    $.each(errores, function(campo, detalles) {
            
                        let mensajesError = ''; // Inicializar la cadena de mensajes de error
                        // Iterar sobre cada detalle de error para concatenar los mensajes
                        $.each(detalles, function(index, detalle) {
                            mensajesError += detalle.message + '<br>'; // Concatenar el mensaje de error con un <br>
                        });
            
                        let $campoInput = $('[name="' + campo + '"]'); // Seleccionar el elemento de formulario por su atributo name                        
                        // Agregar el mensaje de error al elemento de formulario
                        $campoInput.addClass('is-invalid'); // Marcar el campo como inválido
                        $campoInput.next('.invalid-feedback').html(mensajesError); // Agregar el mensaje de error
                    });                    
                } else {
                    alert('Error en el servidor: ' + xhr.responseJSON.msg_error);
                }
            }
        });
    });

    $('#form-entidad').on('reset', function(event) {
        $(this).find('select, input, textarea').removeClass('is-invalid');
        $(this).removeClass('was-validated');
    });
});