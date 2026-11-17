class Road:
    def __init__(self, road_id, highway, name):
        self.road_id = road_id
        self.highway = highway
        self.name = name

    def __repr__(self):
        return f"Road(road_id={self.road_id!r}, highway={self.highway!r}, name={self.name!r})"

    def is_named(self):
        return self.name is not None

    def is_drivable(self):
        return self.highway not in ("footway", "steps", "pedestrian")

fc_road = Road(1, "primary", "FC Road")
baner_road = Road(2, "residential", "Baner Road")
no_name = Road(3, "service", None)
not_drivable = Road(4, "steps", None)

print(fc_road)
print(baner_road.name)
print(no_name.name)
print(fc_road.is_named())
print(no_name.is_named())
print(fc_road.is_drivable())
print(not_drivable.is_drivable())