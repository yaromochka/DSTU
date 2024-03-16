data segment
    a dw 10
    b dw 20
    c dw 30
    x dw ?
data ends
code segment
    assume cs: code, ds: data
    start:
        mov ax, data
        mov ds, ax         ; load addresses

        mov ax, a         ; data segment
        mov bx, b
        add ax, bx           ; A+B
        mov bx, b
        mul bx         ; B*(A+B)
        mov bx, 2           ; 2
        sub bx, ax          ; 2 - B*(A+B)
        mov cx, c
        sar cx, 2          ; C/4
        add bx, cx          ; 2 - B*(A+B) + C/4
        mov x, bx


    quit:
        mov ax, 4c00h   ; end code 0
        int 21h       ; exit into dos
    end start
code ends




