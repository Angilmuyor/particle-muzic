package cat.ifae.phenomena.viz.particle;

import cat.ifae.phenomena.viz.data.MyParticleData;
import cat.ifae.phenomena.viz.cicle.CurrentCicle;
import cat.ifae.phenomena.viz.shapes.MyShape;
import cat.ifae.phenomena.viz.shapes.MyWaveRing;
import cat.ifae.phenomena.viz.shapes.MyWaveDisc;
import cat.ifae.phenomena.viz.params.MyParams;

import processing.core.PApplet;

import java.util.ArrayList;

public class MyBaryon extends MyParticleFamily{

    public MyBaryon(PApplet p, float x, float y, MyParticleData particleData){
        super(p, x, y, particleData);
        addMyShapes();
    }

    @Override
    public void addMyShapes(){
        shapes = new ArrayList<MyShape>();
        int j = 0;
        for (String q: particleData.getComposition()) {
            myParams = new MyParams(p, particleData,q,j);
            currentCicle = new CurrentCicle(p, myParams.quark.getSpeed());
            shapes.add(new MyWaveRing(p,x,y,currentCicle,myParams.quark));
            j++;
        }
        p.println(myParams.quark);
        p.println(myParams.gluon.getColor());
        shapes.add(new MyWaveDisc(p,x,y,myParams.gluon));
    }

    @Override
    public void display(){
        p.text(particleData.getName(), x, y);
        p.blendMode(PApplet.ADD);
        for (MyShape shape: shapes){
            shape.display();
        }
    }

    @Override
    public void move(){
        for (MyShape shape: shapes){
            shape.move();
        }
    }

}