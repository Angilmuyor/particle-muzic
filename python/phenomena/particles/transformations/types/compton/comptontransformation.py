from phenomena.particles.transformations.types import Transformation
from phenomena.particles.sources import ParticleDataSource

class ComptonEffect(Transformation):

    INPUT = ['gamma']
    OUTPUT = ['gamma', 'e-']
    TARGET = 'e-'

    def __init__(self, particle):
        self._particle = particle
        self._values = {}
        if  self._particle.name in ComptonEffect.INPUT:
            self._buildTransfValues()

    def _outputParticles(self):
        return [(1.0,ComptonEffect.OUTPUT)]
        #return [(1.0, map(ParticleDataSource.getPDGId, ComptonEffect.OUTPUT)) ]


    def _transfTime(self):
        return 1
