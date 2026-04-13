#include <stdio.h>
#include <ctype.h>

int is_valid_ip(char ip[]) {
    int num = 0;
    int dots = 0;
    int digits = 0;

    for (int i = 0; ip[i] != '\0'; i++) {

        if (isdigit(ip[i])) {
            num = num * 10 + (ip[i] - '0');
            digits++;

            if (num > 255) {
                return 0;
            }

        } else if (ip[i] == '.') {

            if (digits == 0) {
                return 0;
            }

            dots++;
            num = 0;
            digits = 0;

        } else {
            return 0;
        }
    }

    return dots == 3 && digits > 0;
}

int is_valid_port(int port) {
    return port >= 1 && port <= 65535;
}

int main() {
    int choice;
    char ip[50];
    int port;

    char logg[100][100];
    int log_index = 0;

    while (1) {
        printf("\n=== NÄTVERKSVERKTYG ===\n");
        printf("1. Validera IP-adress\n");
        printf("2. Validera port\n");
        printf("3. Visa logg\n");
        printf("4. Avsluta\n");
        printf("Val: ");
        scanf("%d", &choice);

        if (choice == 1) {
            printf("Ange IP-adress: ");
            scanf("%s", ip);

            if (is_valid_ip(ip)) {
                printf("IP-adressen är giltig.\n");
                sprintf(logg[log_index++], "IP %s - giltig", ip);
            } else {
                printf("IP-adressen är ogiltig.\n");
                sprintf(logg[log_index++], "IP %s - ogiltig", ip);
            }

        } else if (choice == 2) {
            printf("Ange port: ");
            scanf("%d", &port);

            if (is_valid_port(port)) {
                printf("Porten är giltig.\n");
                sprintf(logg[log_index++], "Port %d - giltig", port);
            } else {
                printf("Porten är ogiltig.\n");
                sprintf(logg[log_index++], "Port %d - ogiltig", port);
            }

        } else if (choice == 3) {
            printf("\n=== LOGG ===\n");
            for (int i = 0; i < log_index; i++) {
                printf("%d. %s\n", i + 1, logg[i]);
            }

        } else if (choice == 4) {
            printf("Avslutar...\n");
            break;

        } else {
            printf("Felaktigt val.\n");
        }
    }

    return 0;
}

