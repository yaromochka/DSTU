data segment
    array dw 1, 1, 1, 1, 1, 1
    x dw ?
    count dw 0 ; Исправлено значение count
data ends

code segment
    assume cs: code, ds: data

start:
    mov ax, data
    mov ds, ax

    lea bx, array   ; берём в bx адрес первого элемента
    mov cx, 6 ; длина массива
    xor dx, dx ; Инициализация dx нулями перед суммированием

beg:
    mov ax, [bx]
    add dx, ax
    jmp next
next:
    add bx, 2
    loop beg

quit:
    mov ax, dx
    idiv count
    mov x, ax
    mov ax, 4c00h   ; end code 0
    int 21h
code ends
end start
