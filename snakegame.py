#include<stdio.h>
#include<stdlib.h>
#include<conio.h>

void setup();
void draw();
void input();
void mainlogic();
int tailx[100], taily[100];
int piece=0;
int i ,j ,height=30 , width=50;
int x,y,obx,oby,flag,gameend,score;

int main(){
	setup();
	while (gameend != 1) {
		input();
		draw();
		mainlogic();
		
		usleep(1000);
	
	}
	
}

void mainlogic(){
	
	int i , x1 ,y1 ,x2 ,y2;
	x1 = tailx[0];
	y1 = taily[0];
	tailx[0]=x;
	taily[0]=y;
	for ( i = 1; i <= piece ; i++){
		x2=tailx[i];
		y2=taily[i];
		tailx[i]=x1;
		taily[i]=y1;
		x1=x2;
		y1=y2;
	}
	switch(flag){
		case 1: {
			x--;
			break;
		}
		case 2: {
			x++;
			break;
		}
		case 3: {
			y--;
			break;
		}
		case 4: {
			y++;
			break;
		}
	}
	if ( x==0 || x==height-1 || y == 0 || y == width-1){
		gameend = 1;
	}
	if( x == obx && y == oby ){
		
	label3:
		obx=rand()%30;
		if( obx == 0 )
		goto label3;
		
		label4:
		oby=rand()%50;
		if( oby == 0 )
		goto label4;
		
		piece++;
	}
}

void input(){
	
	if (kbhit()){
		 switch(getch()){
		 	
		 	case 'w': {
		 		flag = 1;
				break;
			 }
		 
		 	case 's': {
		 		flag = 2;
				break;
			 }
		 	
		 	case 'a': {
		 		flag = 3;
				break;
			 }
		 	
		 	
		 	case 'd': {
		 		flag = 4;
				break;
			 }
		 	
		 
}
}
}
void setup(){
	x = height/2;
	y = width/2;
	
	label1:
		obx=rand()%30;
		if( obx == 0 )
		goto label1;
		
		label2:
		oby=rand()%50;
		if( oby == 0 )
		goto label2;
		
	gameend = 0;
	score = 0;
	piece = 0;
}

void draw(){
	int k;
	system("cls");
	for( i=0 ; i < height ; i++){
		for( j=0 ; j < width; j++){
			if( i == 0 || i == height - 1 || j == 0 || j == width-1){
			printf("*");
		}else{
			if( i == x && j == y){
				printf("0");
			}
			else if ( i == obx  && j == oby ){
				printf("@");
			}else{
				for( k=0 ; k<piece ; k++){
					if( i == tailx[k] && j == taily[k]){
						printf("o");
					}
				}
				printf(" ");
			}	
		}
		}
		printf("\n");
	}
}
