class MagicToyCatalog:
    def __init__(self):
        self.toys = {}
        self._secret_offer = "Free plushie with any purchase!"

    def __setitem__(self, name, details):
        """Add/update toys like catalog['RoboDog'] = (49.99, 'RC dog')"""
        self.toys[name] = details

    def __getitem__(self, name):
        """Get toy details using catalog['RoboDog']"""
        return self.toys.get(name, ("Unknown", "Not in stock"))

    def __delitem__(self, name):
        """Remove items with del catalog['RoboDog']"""
        if name in self.toys:
            del self.toys[name]
            print(f"Poof! {name} vanished from the catalog!")
        else:
            raise MagicToyError(f"✨ {name} doesn't exist in our dimension")

    def __contains__(self, name):
        """Check existence with 'RoboDog' in catalog"""
        return name in self.toys

    def __len__(self):
        """Get count with len(catalog)"""
        return len(self.toys)

    def __iter__(self):
        """Iterate with for toy in catalog"""
        return iter(self.toys.items())

    def __add__(self, other):
        """Combine catalogs: mega_catalog = catalog1 + catalog2"""
        combined = MagicToyCatalog()
        combined.toys = {**self.toys, **other.toys}
        return combined

    def __str__(self):
        """User-friendly display"""
        header = "🔮 Magic Toy Catalog 🔮\n"
        items = "\n".join([f"- {name}: ${price} ({desc})"
                          for name, (price, desc) in self.toys.items()])
        return header + (items if items else "✨ Empty (for now)")

    def __repr__(self):
        """Developer representation"""
        return f"<MagicToyCatalog: {len(self)} toys>"

    def __call__(self, discount=0):
        """Activate special offers: catalog(10) for 10% off"""
        return "\n".join([f"{name}: ${price * (1 - discount/100):.2f}"
                         for name, (price, desc) in self.toys.items()])

class MagicToyError(Exception):
    pass
