# flag_shop

Tải source code về, ta thấy đề bài cho chúng ta 3 options. Tuy nhiên, ta cần lưu ý option thứ 2 (vì nó chứa flag).

```python
#include <stdio.h>
#include <stdlib.h>
int main()
{
    setbuf(stdout, NULL);
    int con;
    con = 0;
    int account_balance = 1100;
    while(con == 0){
        
        printf("Welcome to the flag exchange\n");
        printf("We sell flags\n");

        printf("\n1. Check Account Balance\n");
        printf("\n2. Buy Flags\n");
        printf("\n3. Exit\n");
        int menu;
        printf("\n Enter a menu selection\n");
        fflush(stdin);
        scanf("%d", &menu);
        if(menu == 1){
            printf("\n\n\n Balance: %d \n\n\n", account_balance);
        }
        else if(menu == 2){
            printf("Currently for sale\n");
            printf("1. Defintely not the flag Flag\n");
            printf("2. 1337 Flag\n");
            int auction_choice;
            fflush(stdin);
            scanf("%d", &auction_choice);
            if(auction_choice == 1){
                printf("These knockoff Flags cost 900 each, enter desired quantity\n");
                
                int number_flags = 0;
                fflush(stdin);
                scanf("%d", &number_flags);
                if(number_flags > 0){
                    int total_cost = 0;
                    total_cost = 900*number_flags;
                    printf("\nThe final cost is: %d\n", total_cost);
                    if(total_cost <= account_balance){
                        account_balance = account_balance - total_cost;
                        printf("\nYour current balance after transaction: %d\n\n", account_balance);
                    }
                    else{
                        printf("Not enough funds to complete purchase\n");
                    }
                                    
                    
                }
                    
                    
                    
                
            }
            else if(auction_choice == 2){
                printf("1337 flags cost 100000 dollars, and we only have 1 in stock\n");
                printf("Enter 1 to buy one");
                int bid = 0;
                fflush(stdin);
                scanf("%d", &bid);
                
                if(bid == 1){
                    
                    if(account_balance > 100000){
                        FILE *f = fopen("flag.txt", "r");
                        if(f == NULL){

                            printf("flag not found: please run this on the server\n");
                            exit(0);
                        }
                        char buf[64];
                        fgets(buf, 63, f);
                        printf("YOUR FLAG IS: %s\n", buf);
                        }
                    
                    else{
                        printf("\nNot enough funds for transaction\n\n\n");
                    }}

            }
        }
        else{
            con = 1;
        }

    }
    return 0;
}
```

Lựa chọn thứ 2 lại cho chúng ta một offer là real flag và fake flag. Để lấy được real flag ta cần phải thông qua fake flag để lấy thêm money. Vậy làm sao để lấy thêm money? Ta quan sát đoạn code sau:

```python
else if(menu == 2){
            printf("Currently for sale\n");
            printf("1. Defintely not the flag Flag\n");
            printf("2. 1337 Flag\n");
            int auction_choice;
            fflush(stdin);
            scanf("%d", &auction_choice);
            if(auction_choice == 1){
                printf("These knockoff Flags cost 900 each, enter desired quantity\n");
                
                int number_flags = 0;
                fflush(stdin);
                scanf("%d", &number_flags);
                if(number_flags > 0){
                    int total_cost = 0;
                    total_cost = 900*number_flags;
                    printf("\nThe final cost is: %d\n", total_cost);
                    if(total_cost <= account_balance){
                        account_balance = account_balance - total_cost;
                        printf("\nYour current balance after transaction: %d\n\n", account_balance);
                    }
                    else{
                        printf("Not enough funds to complete purchase\n");
                    }
                                    
                    
                }
                    
                    
                    
                
            }
            else if(auction_choice == 2){
                printf("1337 flags cost 100000 dollars, and we only have 1 in stock\n");
                printf("Enter 1 to buy one");
                int bid = 0;
                fflush(stdin);
                scanf("%d", &bid);
                
                if(bid == 1){
                    
                    if(account_balance > 100000){
                        FILE *f = fopen("flag.txt", "r");
                        if(f == NULL){

                            printf("flag not found: please run this on the server\n");
                            exit(0);
                        }
                        char buf[64];
                        fgets(buf, 63, f);
                        printf("YOUR FLAG IS: %s\n", buf);
                        }
                    
                    else{
                        printf("\nNot enough funds for transaction\n\n\n");
                    }}

            }
        }
```

Ta thấy rằng mỗi `fake flag` mất 900$ và nó trừ đi `total_cost` từ `account_balance`. Vậy nếu giá trị `total_cost` âm thì sao? Nếu giá trị `total_cost` âm vừa đủ, ta có thể có được số tiền `account_balance` cực lớn (vì account_balance = account_balance - total_cost;) Vậy làm thế nào để `total_cost` mang giá trị âm?

Chú ý rằng `total_cost` được định nghĩa là một `int`. Đây là một *Signed Integer.* Theo [IBM](https://www.ibm.com/docs/en/aix/7.2?topic=types-signed-unsigned-integers), Signed Integer được thể hiện bằng ký hiệu Two’s Complement (Bù 2) trong máy tính. Trong đó byte quan trọng nhất (MSB) là 0 và ít quan trọng nhất (LSB) là 3. Signed Integer sử dụng bit đầu tiên để xác định đó là số âm hay dương, `0` chỉ số dương và `1` chỉ số âm. Một Signed Integer nằm trong khoảng **[-2147483648 đến 2147483647]**

```
💡 Điều gì xảy ra nếu ta cộng 1 vào 2147483647?

```

```python
>>> numpy.int32(2147483647)
2147483647
>>> numpy.int32(1+2147483647)
-2147483648
```

Quan sát ta thấy rằng khi ta nhập số vượt quá khỏang quy định chúng sẽ quay lại từ đầu giá trị là **-2147483648**. Đây cũng có thể gọi là lỗi **Integer Overflow.** Vậy ta sẽ tận dụng lỗi này để khai thác biến `total_cost`:

```python
>>> 1100 - numpy.int32(2000000*900)
-1799998900
>>> 1100 - numpy.int32(3000000*900) # thoa dk
1594968396
>>> 1100 - numpy.int32(4000000*900) # thoa dk
694968396
```

```python
These knockoff Flags cost 900 each, enter desired quantity
4000000

The final cost is: -694967296

Your current balance after transaction: 694968396

Welcome to the flag exchange
We sell flags

1. Check Account Balance

2. Buy Flags

3. Exit

 Enter a menu selection
2
Currently for sale
1. Defintely not the flag Flag
2. 1337 Flag
2
1337 flags cost 100000 dollars, and we only have 1 in stock
Enter 1 to buy one1
YOUR FLAG IS: picoCTF{m0n3y_bag5_68d16363}
```
