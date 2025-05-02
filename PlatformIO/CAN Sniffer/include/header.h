
#define SEPARATOR ','
#define TERMINATOR '\n'
#define RXBUF_LEN 100

typedef unsigned char byte;

typedef struct {
  long id;
  byte rtr;
  byte ide;
  byte dlc;
  byte dataArray[20];
} packet_t;

void printHex(long num);
void printPacket(packet_t *packet);
void onCANReceive(int packetSize);
void sendPacketToCan(packet_t *packet);
char getNum(char c);
char *strToHex(char *str, byte *hexArray, byte *len);
void rxParse(char *buf, int len);
void RXcallback(void);