#include <iostream>
#include <fstream>
#include <ctime>
#include <RF24/RF24.h>            //Allgemeine Libary f  r NRF24L01+
#include <cstdlib>
#include <sstream>
#include <string>
#include <unistd.h>


using namespace std;

int main() {
    
    
    return 0;
}

int writeToFile () {
    // current date/time based on current system
    time_t now = time(0);
    
    ofstream myfile;
    myfile.open ("data.temp");
    myfile << now << " Writing this to a file.\n"<< "test";
    myfile.close();
    return 0;
}




