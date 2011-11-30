#include <stdio.h>
#include <time.h>

/*
 * + cron or while(1)?
 * - cron.
 * + get time
 * - on_batterie?
 * - pop up window
 */

int main(int argc, char **argv){
    // get time
    time_t time_value = time(NULL);
    struct tm *now = localtime(&time_value);
    int hour = now -> tm_hour;
    int min = now -> tm_min;
    
    
    printf("%d:%d\n", hour, min);
	return 0;
}

