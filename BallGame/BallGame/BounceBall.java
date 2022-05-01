import java.awt.Color;

public class BounceBall extends BasicBall
{
    private double bounceCount;

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


    public void move()
    {        
        rx = rx + vx;
        ry = ry + vy;
        if (Math.abs(rx) > 0.9)
        {
            bounceCount = bounceCount -1;
            if (bounceCount < 0)
            {
                isOut = true;
            }
            vx = -vx;
        }
        else if (Math.abs(ry) > 0.9)
        {            
            bounceCount = bounceCount -1;
            vy = -vy;
            if (bounceCount < 0)
            {
                isOut = true;
            }
        }
    }

    public boolean isHit(double x, double y) {
    	if ((Math.abs(rx-x)<=radius) && (Math.abs(ry-y)<=radius))
        {
            hits = hits+1;
            System.out.println(hits);
			return true;
        }
		else 
        {
            System.out.println(x + "," +y);
            return false; 
        }

    }




    public int getScore() {
    	return 15;
    }

    
}
