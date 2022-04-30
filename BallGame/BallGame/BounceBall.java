import java.awt.Color;

public class BounceBall extends BasicBall
{
    private double bounceCount;
    protected double rx, ry;         // position
    protected double vx, vy;         // velocity

    public BounceBall(double r, Color c)
    {
        super(r,c);
        bounceCount = 3;
        rx = 0.0;
        ry = 0.0;
        vx = StdRandom.uniform(-0.01, 0.01);
        vy = StdRandom.uniform(-0.01, 0.01);
    }

    // move the ball one step
    public void move() {
        
        rx = rx + vx;
        ry = ry + vy;
        if ((Math.abs(rx) > 1.0) || (Math.abs(ry) > 1.0)) 
        {
            bounceCount = bounceCount -1;
            if (bounceCount >0)
            {
                isOut = false;
                System.out.println(isOut);
            }
            else 
            {
                
                System.out.println("testtttttttttt");
                isOut = true;
            }
        }
    }


    public int getScore() {
    	return 15;
    }

    
}
