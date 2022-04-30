import java.awt.Color;

public class ShrinkBall extends BasicBall
{
    private double startingRadius;

    public ShrinkBall(double r, Color c)
    {
        super(r,c);
        startingRadius = r;
    }

    public boolean isHit(double x, double y) {
    	if ((Math.abs(rx-x)<=radius) && (Math.abs(ry-y)<=radius))
        {
            radius = radius*2/3;
            if (radius < 0.25*startingRadius)
            {
                radius = startingRadius;
            }

			return true;
        }
		else return false; 

    }

    public int getScore() {
    	return 20;
    }

    
}
