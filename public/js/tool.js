/**
 * Created by Everson on 18/02/2017.
 */

// Macara Exemplo: onkeypress="mascara(this, '##/##/####');"
function mascara(src, mask) {
    var i = src.value.length;
    var saida = mask.substring(0, 1);
    var texto = mask.substring(i);
    if (texto.substring(0, 1) != saida)
    {
        src.value += texto.substring(0, 1);
    }
}
// So numero Exempo: onkeypress="return SomenteNumero(event)"
function SomenteNumero(e) {
    var tecla = (window.event) ? event.keyCode : e.which;
    if ((tecla > 47 && tecla < 58))
        return true;
    else {
        if (tecla == 8 || tecla == 0)
            return true;
        else
            return false;
    }
}