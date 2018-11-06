import pytest
from phenomena.particles.transformations.types import Transformation, Annihilation
from testparticles import AnnihilationParticle

test_particles = [(AnnihilationParticle("e+", p=2.0))]

@pytest.mark.parametrize("particle",test_particles)
def test_annihilation_basics(particle):
    assert particle.name == "e+"
    alltypes = particle.transformation.allTypes
    thisType = [transf for transf in alltypes if transf['type']=='Annihilation']
    assert thisType[0]['target'] == 'e-'
    assert set(thisType[0]['list'][0][1]) == set(['gamma'])

    output = particle.transformation.output
    assert len(output) == 1

    for outputpart in output:
        assert isinstance(outputpart,UndercoverParticle)
        assert outputpart.E < particle.E

@pytest.mark.parametrize("particle",test_particles)
def test_annihilation_conservation(particle, conservation, resolution, print_particle):
    print_particle
    for attr in ['Pt', 'E','charge', 'baryonnumber', 'leptonnumber']:
        assert round(getattr(conservation.In,attr),resolution) == round(getattr(conservation.Out,attr), resolution)
