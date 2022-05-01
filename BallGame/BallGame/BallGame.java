/******************************************************************************
 *  Compilation:  javac BallGame.java
 *  Execution:    java BallGame n
 *  Dependencies: BasicBall.java StdDraw.java
 *
 *  Creates a BasicBall and animates it
 *
 *  Part of the animation code is adapted from Computer Science:   An Interdisciplinary Approach Book
 *  
 *  Run the skeleton code with arguments : 1  basic  0.08
 *******************************************************************************/
import java.awt.Color;
import java.awt.Font;
import java.util.ArrayList;

public class BallGame { 

    public static void main(String[] args) {
  
    	// number of bouncing balls
    	int numBalls = Integer.parseInt(args[0]);
    	//ball types
    	String ballTypes[] = new String[numBalls];
    	//sizes of balls
    	double ballSizes[] = new double[numBalls];
    	
    	//retrieve ball types
    	int index =1;
    	for (int i=0; i<numBalls; i++) {
    		ballTypes[i] = args[index];
    		index = index+2;
    	}
    	//retrieve ball sizes
    	index = 2;
    	for (int i=0; i<numBalls; i++) {
    		ballSizes[i] = Double.parseDouble(args[index]);
    		index = index+2;
    	}
     
    	//TO DO: create a Player object and initialize the player game stats.  
    	class Player
        {
            String name;
            int score;
            int[] typeHit = {0,0,0};
        }

        Player test = new Player();
        test.name = "Test";
        test.score = 0;

        
    	//number of active balls
    	int numBallsinGame = 0;
        StdDraw.enableDoubleBuffering();

        StdDraw.setCanvasSize(800, 800);
        // set boundary to box with coordinates between -1 and +1
        StdDraw.setXscale(-1.0, +1.0);
        StdDraw.setYscale(-1.0, +1.0);

        // create colored balls 
        //TO DO: Create "numBalls" balls (of types given in "ballTypes" with sizes given in "ballSizes") and store them in an Arraylist
        ArrayList<BasicBall> ballList = new ArrayList<BasicBall>(); // Create an ArrayList object
        String basic[] = {"basic"};
        String shrink[] = {"shrink"};
        String bounce[] = {"bounce"};


        for (int i = 0; i <numBalls; i++)
        {            
            if(ballTypes[i].equals(shrink[0]))
            {
                ShrinkBall ball = new ShrinkBall(ballSizes[i], Color.GREEN);
                ballList.add(ball);
            }
            else if(ballTypes[i].equals(bounce[0]))
            {
                BounceBall ball = new BounceBall(ballSizes[i], Color.YELLOW);
                ballList.add(ball);
            }
            else
            {
                BasicBall ball = new BasicBall(ballSizes[i],Color.BLUE);
                ballList.add(ball);

            }
        }
   		//TO DO: initialize the numBallsinGame
   		numBallsinGame = ballList.size();
        
        // do the animation loop
        StdDraw.enableDoubleBuffering();
        while (numBallsinGame > 0) {

        	// TODO: move all balls
            for(int i = 0; i < numBalls; i++)
            {
                BasicBall volatileBall = (ballList.get(i));
                volatileBall.move();
            }

            //Check if the mouse is clicked
            if (StdDraw.isMousePressed()) {
                double x = StdDraw.mouseX();
                double y = StdDraw.mouseY();
                //TODO: check whether a ball is hit. Check each ball.  
                for(int i = 0; i < numBalls; i++)
                {
                    BasicBall volatileBall = (ballList.get(i));                    
                    if (volatileBall.isHit(x,y)) {
                    	volatileBall.reset();
                    	//TO DO: Update player statistics
                        test.score += volatileBall.getScore();
                        if (ballTypes[i].equals(basic[0]))
                        {
                            test.typeHit[0] += 1;
                        }
                        else if (ballTypes[i].equals(shrink[0]))
                        {
                            test.typeHit[1] += 1;
                        }
                        else if (ballTypes[i].equals(bounce[0]))
                        {
                            test.typeHit[2] += 1;
                        }
                    }
                } 
            }
                
            numBallsinGame = 0;
            // draw the n balls
            StdDraw.clear(StdDraw.GRAY);
            StdDraw.setPenColor(StdDraw.BLACK);
            
            //TO DO: check each ball and see if they are still visible. numBallsinGame should hold the number of visible balls in the game.  

            for(int i = 0; i < numBalls; i++)
            {
                BasicBall volatileBall = ballList.get(i);                    
                if (ballList.get(i).isOut == false)
                { 
                    volatileBall.draw();
                    numBallsinGame++;
                }

            } 



            //Print the game progress
            StdDraw.setPenColor(StdDraw.YELLOW);
            Font font = new Font("Arial", Font.BOLD, 20);
            StdDraw.setFont(font);
            StdDraw.text(-0.65, 0.90, "Number of balls in game: "+ String.valueOf(numBallsinGame));
            //TO DO: print the rest of the player statistics
            StdDraw.text(-0.65, -0.90, "Score: "+test.score);

            StdDraw.show();
            StdDraw.pause(20);
        }
        while (true) {
            StdDraw.setPenColor(StdDraw.BLUE);
            Font font = new Font("Arial", Font.BOLD, 60);
            StdDraw.setFont(font);
            StdDraw.clear(StdDraw.GRAY);
            StdDraw.text(0, 0, "GAME OVER");
            //TO DO: print the rest of the player statistics
            String maxType;
            if (test.typeHit[0] > test.typeHit[1] && test.typeHit[0] > test.typeHit[2])
            {
                maxType = "Basic";
            }
            else if (test.typeHit[1] > test.typeHit[0] && test.typeHit[1] > test.typeHit[2])
            {
                maxType = "Shrink";
            }
            else if (test.typeHit[2] > test.typeHit[0] && test.typeHit[2] > test.typeHit[1])
            {
                maxType = "Bounce";
            }
            else
            {
                maxType = "Tie";
            }



            StdDraw.text(0, 0.50, "Score: "+test.score);
            StdDraw.text(0, -0.50,"Type hit most: " + maxType);
            StdDraw.show();
            StdDraw.pause(10);           
        }
        	
        
    }
}