---
name: Introduction to the Layout API
type: topic
kit: special_topics
brief: "Haiku's Layout API is centered around the BLayoutItem and BLayout classes"
source: haiku-book
---

# Introduction to the Layout API
## Description

Haiku's Layout API is centered around the [BLayoutItem](../interface_kit/classBLayoutItem.md) and [BLayout](../interface_kit/classBLayout.md) classes. The [BLayoutItem](../interface_kit/classBLayoutItem.md) class represents thing that can be managed by a [BLayout](../interface_kit/classBLayout.md), which is itself a [BLayoutItem](../interface_kit/classBLayoutItem.md). Before we go any further, it is a good idea to familiarize yourself with the different [BLayout](../interface_kit/classBLayout.md) classes available in Haiku: 


* [BGroupLayout](classBGroupLayout.md)

* [BGridLayout](classBGridLayout.md)

* [BCardLayout](../interface_kit/classBCardLayout.md)

* [BSplitView](classBSplitView.md)



You'll notice that [BSplitView](classBSplitView.md) is not actually a [BLayout](../interface_kit/classBLayout.md), but a [BView](../interface_kit/classBView.md). The [BSplitView](classBSplitView.md) class uses a custom [BLayout](../interface_kit/classBLayout.md) behind the scenes, but because it must also be able to draw, a [BView](../interface_kit/classBView.md) is required. Other [BLayout](../interface_kit/classBLayout.md) objects have [BView](../interface_kit/classBView.md) objects that can be used for convenience. 


* [BGroupLayout](classBGroupLayout.md) : [BGroupView](../interface_kit/classBGroupView.md)

* [BGridLayout](classBGridLayout.md) : [BGridView](classBGridView.md)

* [BCardLayout](../interface_kit/classBCardLayout.md) : [BTabView](../interface_kit/classBTabView.md) (also provides on-screen tabs)



Although it is not necessary to use these classes to make use of the corresponding layouts, it does make things easier.


Once you have an understanding of what each [BLayout](../interface_kit/classBLayout.md) does, you can start designing an interface with them. Let's consider a very simple window, with a single item in the center. For this, any of the layouts mentioned above would work, but we'll use a [BGroupLayout](classBGroupLayout.md), because it suits this purpose the best.


The [BGroupLayout](classBGroupLayout.md) constructor is:



```cpp
BGroupLayout(orientation orientation, float spacing = B_USE_DEFAULT_SPACING)
```

Because we only have one item in this layout, `orientation` and `spacing` become irrelevant. Let's choose B_VERTICAL for `orientation`, and leave `spacing` at its default.



```cpp
BGroupLayout* group = new BGroupLayout(B_VERTICAL);
BWindow* window = MakeWindow();
window->SetLayout(group);
```

Before we can add anything to our layout, we must attach it to something, and here we've used the [BWindow::SetLayout()](../interface_kit/classBWindow.md#ad0e630f2691a0f7919b809b7ea265095) method to accomplish that. By doing this, `window` takes ownership of `group`, so there is no need to manually `delete group` when we're done with it.


Now that we've got our [BGroupLayout](classBGroupLayout.md) in place, we can start adding things to it, so let's add a [BStringView](../interface_kit/classBStringView.md).



```cpp
group->AddView(MakeStringView("Haiku rocks!"));
```

Now we've got a [BWindow](../interface_kit/classBWindow.md) with a horizontal [BGroupLayout](classBGroupLayout.md) holding a single [BView](../interface_kit/classBView.md). However, if we want to ensure that our [BStringView](../interface_kit/classBStringView.md) is always centered in the window, we should give it an explicit [BAlignment](../interface_kit/classBAlignment.md). So the last line becomes:



```cpp
BLayoutItem* stringView = group->AddView(MakeStringView("Haiku rocks!"));
stringView->SetExplicitAlignment(BAlignment(B_ALIGN_HORIZONTAL_CENTER,
    B_ALIGN_VERTICAL_CENTER);
```

Now our [BStringView](../interface_kit/classBStringView.md) will always be right in the middle of the space allotted to it, which at the moment is the whole of `window`.


Now let's add a [BMenuBar](../interface_kit/classBMenuBar.md):



```cpp
group->AddView(0, MakeMenuBar());
group->SetInsets(0, 0, 0, 0);
```

Because we want our [BMenuBar](../interface_kit/classBMenuBar.md) to appear at the very top of the window, we have to insert it at index `0`, above the [BStringView](../interface_kit/classBStringView.md) we added earlier. We also use [BTwoDimensionalLayout::SetInsets()](classBTwoDimensionalLayout.md#acaf4ec650969994cb39dd015e3bebd91) to make sure that our [BMenuBar](../interface_kit/classBMenuBar.md) is flush to the edges of `window`. We also want a bit of space between our [BMenuBar](../interface_kit/classBMenuBar.md) and our [BStringView](../interface_kit/classBStringView.md), but `group's` spacing has already been set by the [BGroupLayout](classBGroupLayout.md) constructor, so we don't need to do that.


Now that we've put our [BGroupLayout](classBGroupLayout.md) to good use, we can rest easy, assured that GUI will always look nice, no matter what font is used, or how big or little `window` is stretched. Of course, very few interfaces are as simple as this one.


The layout classes can deal with complex layouts. Suppose, for example, that we wanted to add a grid of BButtons under our [BStringView](../interface_kit/classBStringView.md). We could use a [BGridLayout](classBGridLayout.md) for this. The [BGridLayout](classBGridLayout.md) constructor is:



```cpp
BGridLayout(float horizontal = B_USE_DEFAULT_SPACING,
 float vertical = B_USE_DEFAULT_SPACING);
```

Because we want a bit of breathing room between our buttons, we'll leave vertical and horizontal spacing as is.



```cpp
BGridLayout* grid = new BGridLayout();
group->AddItem(grid);
```

You'll notice that we've added `grid` directly to `group`. This means that any [BView](../interface_kit/classBView.md) objects we add to `grid` will become children of `window`, but will be positioned by `grid`.



```cpp
grid->AddView(MakeSmallButton(), 0, 0);
grid->AddView(MakeSmallButton(), 1, 0);
grid->AddView(MakeBigButton(), 0, 1, 2, 1);
grid->AddView(MakeSmallButton(), 1, 2);
```

Now we've got a nice grid of [BButton](../interface_kit/classBButton.md) objects, let's go over it quickly: 


* `grid` has two columns and three rows.

* The cells (0, 0), (1, 0), and (1, 2) hold small buttons

* The cells (0, 1) and (1, 1) hold a single button that spans both cells.

* The cell (0, 2) is empty.



One of the features you'll find incredibly handy in the layout API is the builders in [LayoutBuilder.h](LayoutBuilder_8h.md). Here's how our whole layout would look if it were done with these builders:



```cpp
BLayoutBuilder::Group<>(window, B_VERTICAL)
    .SetInsets(0, 0, 0, 0)
    .Add(MakeMenuBar())
    .Add(MakeStringView("Haiku rocks!"))
    .AddGrid()
        .Add(MakeSmallButton(), 0, 0)
        .Add(MakeSmallButton(), 1, 0)
        .Add(MakeBigButton(), 0, 1, 2, 1)
        .Add(MakeSmallButton(), 1, 2);
```

This is only one way that you could build this layout, but it is probably the most succinct. Functionally, this is equivalent to all the previous code in this introduction.


Special Handling for BBox[BBox](../interface_kit/classBBox.md) is a "container" view that can contain other views. The use of the layout manager within an instance of [BBox](../interface_kit/classBBox.md) is a special case. Code such as is shown below is necessary to automatically layout views within a [BBox](../interface_kit/classBBox.md).

```cpp
BBox *box = new BBox("box-example");
BGroupLayout *boxLayout = BLayoutBuilder::Group<>(B_HORIZONTAL)
    .Add(button1)
    .Add(button2);
 
box->AddChild(boxLayout->View());
```

Generated from the [Haiku Book API docs](https://www.haiku-os.org/docs/api/layout_intro.html).
