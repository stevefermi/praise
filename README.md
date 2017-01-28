# Python Praise

Build friendly Python packages that praise their users if they have done something good, or they just need it to feel better.

### Installation

Use pip to install this package.
```
pip install praise
```

### Usage

```
import praise
praise()
praise("You have ${created} a good ${package}!")
```

if you want to get the praise string, try this:
```
import praise
praise_string=parse_template("You have ${created} a good ${package}!")
```

### License

MIT