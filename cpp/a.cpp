#include <iostream>
#include <thread>
#include <unistd.h>
#include <chrono>
#include <mutex>              // std::mutex, std::unique_lock
#include <condition_variable> // std::condition_variable



class S  {
    static S* singletonInstance ;
    static std::once_flag singleton_flag;

    static void init_singleton() {
        singletonInstance = new S ;
    }

    public:
    static S* getSingletonInstance() {
        std::call_once(singleton_flag, init_singleton);
        return singletonInstance;
    }
} ;

std::once_flag S::singleton_flag ;
S* S::singletonInstance = 0 ;

int fib(int i) {
    if (i==0) return 1 ;
    if (i==1) return 1 ;
    int i0=1 ;
    int i1=1 ;
    int i2=2 ;
    for (int j=2;j<=i;j++) {
        i2 = i0 + i1 ;
        i0 = i1 ;
        i1 = i2 ;
    }
    return i2 ;
}

std::mutex mtx_foo, mtx_bar ;
std::condition_variable cv ;
bool ready_foo = false;
bool ready_bar = false;

bool block_foo = true;
bool block_bar = true;

int boss() {
    ready_foo = true ;
    ready_bar = true ;
    while (true) {
        if ( ready_foo && ready_bar ) {
            std::cout << "boss sees everybody ready" << std::endl ;
            std::this_thread::sleep_for(std::chrono::milliseconds(3000));
            block_foo = false;
            block_bar = false ;
        }

    }
}

int foo() {
    while (true) {
        while (block_foo) {
            // std::cout << "foo waits" << std::endl ;
            std::this_thread::sleep_for(std::chrono::milliseconds(50));
        }
        block_foo = true ;
        ready_foo = false ;
        for (int i=0;i<10;++i) {
            std::cout << "foo " << i << std::endl ;
            std::this_thread::sleep_for(std::chrono::milliseconds(1000));
        }
        block_foo = true ;
        ready_foo = true ;
    }
}

int bar(int x) {
    while (true) {
        while (block_bar) {
            //std::cout << "bar waits" << std::endl ;
            std::this_thread::sleep_for(std::chrono::milliseconds(50));
        }
        block_bar = true ;
        ready_bar = false ;
        for (int i=0;i<10;++i) {
            std::cout << "bar " << i << std::endl ;
            std::this_thread::sleep_for(std::chrono::milliseconds(3000));
        }
        block_bar = true ;
        ready_bar = true ;
   }
}



int main(int argc,char** argv) {
    std::cout << "hello world" << std::endl ;
    S* s = S::getSingletonInstance() ;
    std::cout << fib(6) << std::endl ;
    std::thread first (foo);     // spawn new thread that calls foo()
    std::thread second (bar,0);  // spawn new thread that calls bar(0)

    boss() ;
    first.join();                // pauses until first finishes
    second.join();               // pauses until second finishes

    std::cout << "foo and bar completed.\n";

    return 0 ;
}