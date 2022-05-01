import java.awt.Color;

public class SplitBall extends BasicBall
{

    public SplitBall(double r, Color c)
    {
        super(r,c);
    }

    public boolean isHit(double x, double y) {
    	if ((Math.abs(rx-x)<=radius) && (Math.abs(ry-y)<=radius))
        {
            //update and reset
            hits = hits+1;
            vx = StdRandom.uniform(-0.01, 0.01); //randomize speed on each hit
            vy = StdRandom.uniform(-0.01, 0.01);

			return true;
        }
		else return false; 

    }

}