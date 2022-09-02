from typing import List


class Segment:
    def __init__(self, departure: str, destination: str) -> None:
        self.departure = departure
        self.destination = destination


class Flight:
    def __init__(self, segments: List[Segment]) -> None:
        self.segments = segments
        
    def __repr__(self) -> str:
        stops = [self.segments[0].departure, self.segments[0].destination]
        for segment in self.segments[1:]:
            stops.append(segment.destination)
        return '->'.join(stops)
      
    @property  
    def depature_point(self) -> str:
        return self.segments[0].departure
    
    @depature_point.setter
    def depature_point(self, departure: str):
        # self.segments[0].departure = value
        destination = self.segments[0].destination 
        self.segments[0] = Segment(departure=departure,
                                   destination=destination)

    
if __name__ == "__main__":
    flight = Flight(segments=[Segment('GLA', 'LHR')])
    print(flight.depature_point)
    flight.depature_point = "EDI"
    print(flight.depature_point)
    print(flight.segments[0].destination)
    