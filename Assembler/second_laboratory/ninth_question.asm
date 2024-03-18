data segment
    array dw 7, 13, 15, 6, 14, 34
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
    add count, 1
    jmp next
next:
    add bx, 2
    loop beg

quit:
    mov ax, dx
    mov bx, count
    xor dx, dx
    div bx ; dx:ax = ax / bx
    mov x, ax
    mov ax, 4c00h   ; end code 0
    int 21h
code ends
end start
