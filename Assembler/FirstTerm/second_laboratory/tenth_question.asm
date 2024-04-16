data segment
    array dw 17,0,12,479,-347,40,50,7,4,97 ; 10 элементов по 16 бит
    count dw 0 ; счётчик
data ends

code segment
    assume cs: code, ds: data;

start:
     mov ax, data
     mov ds, ax

     lea bx, array   ; начало массива
     mov cx, 10      ; длина массива

beg:
    mov ax, [bx]    ; перекладываем число из массива в ax
    cmp ax, 10h     ; сравниваем число с 10h (16)
    jg GreaterThan10   ; переходим к функции сравнения

    jmp next         ; пускай цикл далоьше

GreaterThan10:
    add count, 1

next:
    add bx, 2
    loop beg         ; начало цикла

quit:
    mov ax, 4c00h
    int 21h
code ends
end start