# -*- coding: utf-8 -*-

import os

def lorem_ipsum():
    return \
"""Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce pretium purus et odio tincidunt, ac laoreet enim volutpat. Donec lacus tortor, lacinia eu orci nec, aliquam ornare eros. Aliquam mollis magna ut metus convallis vulputate. Mauris eget rutrum nibh, vitae varius metus. Vestibulum malesuada imperdiet tellus, non tristique quam aliquam in. Aliquam at nulla eget diam pellentesque tincidunt sed vitae ligula. Nam posuere est felis, eu consequat tortor faucibus id. Mauris gravida est vitae purus ultrices, eu pharetra ante posuere. Proin venenatis urna ut volutpat sollicitudin. Donec in justo et arcu tempus lobortis. Quisque facilisis adipiscing augue vitae hendrerit.

Pellentesque ultricies nulla at ante volutpat, sit amet elementum magna tincidunt. Fusce magna arcu, semper at lacus ac, tincidunt dapibus mi. Nulla non sapien sed elit gravida volutpat. Donec ac viverra tortor. Nam ultrices justo quis nisl semper, eget blandit eros euismod. Proin leo elit, hendrerit eget leo faucibus, interdum aliquet lacus. Ut rhoncus diam dui, quis accumsan augue viverra eget. Praesent blandit orci odio, vitae elementum arcu congue vel. Integer in nibh eget lectus laoreet consequat.

Morbi ullamcorper eget mi ac mattis. In hac habitasse platea dictumst. Suspendisse dignissim orci a tellus imperdiet consequat. Cras a placerat dui, eget elementum elit. Maecenas lacinia turpis et dui pharetra semper. Nunc fringilla neque scelerisque orci fringilla lobortis. Donec ac ornare dui. Sed viverra eget arcu id aliquam. Nullam eleifend at augue ut egestas. Suspendisse blandit enim id semper bibendum. Fusce quis interdum elit. Pellentesque nec diam nec elit commodo iaculis. Maecenas lobortis mauris facilisis velit varius, id interdum sapien eleifend. Nam feugiat ante id velit ultrices mattis. Donec ut arcu tortor. Mauris id mollis augue.

Donec aliquam, felis quis eleifend vestibulum, purus ante semper sapien, nec sagittis diam nibh eu velit. Cras sed iaculis diam. Morbi nisl odio, dictum non cursus ut, vehicula in metus. Vestibulum lobortis ut lectus ut consectetur. Donec nisi odio, mollis in pharetra eget, auctor et felis. Nam rhoncus dictum dolor, sed dapibus est sollicitudin quis. Donec sit amet pharetra ligula. Aliquam suscipit molestie nisi ac condimentum. Cras vel leo iaculis, vestibulum felis non, egestas tellus. Vestibulum imperdiet sagittis velit, non eleifend erat ultricies sit amet. Morbi non suscipit massa. Cras et nibh vel tortor pulvinar ornare.

Aenean leo dui, bibendum nec porttitor euismod, tempus sed sapien. Nunc sagittis quis nunc quis rutrum. Suspendisse nec nulla non enim aliquet interdum. In luctus ligula eget metus auctor rhoncus. Nulla vel dapibus mi, at bibendum ipsum. Nam vitae lectus volutpat, luctus elit non, bibendum tortor. Nunc non ultrices eros. Etiam elementum aliquam massa ac ullamcorper. Ut viverra vitae lacus sed feugiat. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae;""".strip()


class Category:
    def __init__( self, name, priority=1.0 ):
        self.name = name
        self.priority = priority
        self.ordinal = 0

    def __repr__( self ):
        return "Kategori<{0}>".format( self.name )

    def set_ordinal( self, n ):
        self.ordinal = n


class Entry:
    def __init__( self, title, category_names=None, tag_names=None ):
        self.title = title
        self.categories = set()
        self.tag_names = []

    def set_categories( self, categories ):
        for c in categories:
            self.categories.add( c )

    def set_tags( self, tag_names ):
        self.tag_names = tag_names


    def __str__( self ):
        return "[Entry: \"{title}\"] -> ({categories})".format(title=self.title, categories=self.categories)


class Categories:

    def __init__( self ):
        self.categories = {}

    def __setitem__( self, key, value ):
        self.categories[key] = value

    def __getitem__( self, category_name ):
        return self.categories.get( category_name )

    def __call__( self, category_name ):
        return self.categories.get( category_name )

    def __list__(self):
        return [v for k, v in self.categories.values()]

    def __iter__(self):
        return self.categories.values().__iter__()

    def __len__( self ):
        return len( self.categories )


class Entries:
    def __init__( self ):
        self.entries = []

    def __lt__( self, entry ):
        self.entries.append( entry )

    def __iter__( self ):
        return self.entries.__iter__()

    def __len__( self ):
        return len( self.entries )

    def create_in_categories( self, categories, category_names, *args ):
        if len(args):
            for entry in args:
                for n in category_names:
                    entry.categories.add( categories[n] )
                    self.entries.append( entry )

class E(Entry):
    pass

class C(Category):
    pass


if __name__ == "__main__":

    categories = Categories()

    category_definitions = [
        ( "prosjekter",                 0.625 ),
        ( "utviklingsplatformer",        0.625 ),
        ( "funksjonelle områder",       0.625 ),
        ( "arrangementer",              0.625 ),
        ( "instrumenter og verktøy",    0.625 ),

        ( "programvare",                0.250 ),
        ( "samarbeidspartnere",         0.250 ),
        ( "foredragsholdere",           0.250 ),
        ( "severdigheter",              0.250 ),

        ( "medlemmer",                  0.125 ),
        ( "prosjektideer",              0.125 ),
        ( "materialer",                 0.125 ),
        ( "spesielle komponenter",      0.125 )
    ]


    print "Number of categories: ", len( category_definitions )


    for name, priority in category_definitions:
        categories[name] = C(name, priority)

    entries = Entries()

    entries.create_in_categories(

        categories,

        [ 'prosjektideer'],

        E(
            'OpenRC'
        ),

        E(
            'Husroboten'
        ),

        E(
            'Gigakaeder'
        ),

        E(
            'Gear train'
        ),

    )


    entries.create_in_categories(

        categories,

        [ 'funksjonelle områder' ],

        E(
            'Loddestasjon'
        ),

        E(
            'Wiki'
        ),

        E(
            'Blader, papers og bøker'
        ),

        E(
            'Sofahjørnet'
        ),

        E(
            'Roteboksen'
        ),

        E(
            'Utstilling'
        ),

    )

    entries.create_in_categories(

        categories,

        ['programvare'],

        E(
            'Arduino'
        ),

        E(
            'Illustrator/Adobe Creative Suite'
        ),

        E(
            'Processing'
        ),

        E(
            'Android'
        ),

        E(
            'FinalCut Pro'
        ),

        E(
            'NetLogo'
        ),

    )


    entries.create_in_categories(

        categories,

        ['medlemmer'],

        E(
            'Ilya Kostolomov'
        ),

        E(
            'Bao Marianna Nguyen'
        ),

        E(
            'Persijn D. Kwekkeboom'
        ),

        E(
            'Srod Karim',
            'Utvikleren bak spill som Suburban Karate Warrior og Banana Hero'
        ),

        E(
            'Fredrik Hov'
        ),

        E(
            'Asgeir Mortensen'
        ),

        E(
            'Jan Ole Skotterud'
        ),

        E(
            'Fredrik Hov'
        ),

    )

    entries.create_in_categories(

        categories,

        ['medlemmer', 'foredragsholdere'],

        E(
            'Kyrre Havik Eriksen'
        ),

        E(
            'Sigmund Hansen'
        ),

        E(
            'Veronika Heimsbak'
        ),

        E(
            'Jonathan Ringstad'
        ),

        E(
            'Roger Antonsen'
        ),

    )




    entries.create_in_categories(

        categories,

        ['foredragsholdere'],

        E(
            'Tom Igoe'
        ),

    )



    entries.create_in_categories(

        categories,

        ['prosjekter'],

        E(
            'Den fullstendige maskinen'
        ),

        E(
            'Krydderino'
        ),

        E(
            'Pink Ardubot'
        ),

        E(
            'Babybot'
        ),

        E(
            'B.L.I.M.P.'
        ),

    )



    entries.create_in_categories(
        categories,

        ['prosjekter', 'utviklingsplatformer'],

        E(
            'Arkademaskina'
        ),

        E(
            'Game of Light'
        ),

        E(
            'Turtlebot'
        ),

    )



    entries.create_in_categories(
        categories,

        ['utviklingsplatformer'],

        E(
            'Pleo'
        ),

        E(
            'Quadcopter'
        ),

        E(
            'E-puck'
        ),

        E(
            'DFRobot-platformen (Thinkee Winkee)'
        ),

        E(
            'Commodore64'
        ),

        E(
            'Energy Micro'
        ),

        E(
            'Arduino'
        ),

        E(
            'Raspberry Pi'
        ),

        E(
            'Fignition'
        ),

        E(
            'Gameduino'
        ),

        E(
            'Diverse robotplatformer'
        ),

        E(
            'Emotiv'
        ),

        E(
            'Infoskjerm'
        ),

    )



    entries.create_in_categories(
        categories,

        ['instrumenter og verktøy'],

        E(
            'Weller WD-1'
        ),

        E(
            'Rigol 1102A'
        ),

        E(
            'Ultimaker'
        ),

        E(
            'Makerbot'
        ),

        E(
            'Printrbot'
        ),

        E(
            'Plastknekker'
        ),

        E(
            'Foto- og videoutstyr'
        ),

        E(
            'GoPro'
        ),

        E(
            'Lydutstyr'
        ),

    )



    entries.create_in_categories(
        categories,

        ['materialer'],

        E(
            'Tøy'
        ),

        E(
            'MakerBeam'
        ),

        E(
            'Mecano'
        ),

        E(
            'Plast'
        ),

        E(
            'Generiske El-komponenter'
        ),

        E(
            'PCB/stripeboards'
        ),

    )



    entries.create_in_categories(
        categories,

        ['samarbeidspartnere'],

        E(
            'Robotica Osloensis'
        ),

        E(
            'Statoil'
        ),

        E(
            'The Gathering'
        ),

        E(
            'Lær kidsa kode'
        ),

        E(
            'Teknisk museum'
        ),

        E(
            'Telemuseet'
        ),

    )



    entries.create_in_categories(
        categories,

        ['severdigheter'],

        E(
            'Eggbot'
        ),

        E(
            'Rubiks kube'
        ),

        E(
            'Singularity Chess'
        ),

        E(
            'LittleBits'
        ),

        E(
            'Romo'
        ),

        E(
            'Sifteo'
        ),

        E(
            'Zome'
        ),

        E(
            'Hexbug'
        ),

    )



    entries.create_in_categories(
        categories,

        ['spesielle komponenter'],

        E(
            'Sensorer'
        ),

        E(
            'Motorer/aktuatorer'
        ),

        E(
            'Batterier'
        ),

    )



    entries.create_in_categories(
        categories,

        ['arrangementer'],

        E(
            'GameJam'
        ),

        E(
            'Campus TG'
        ),

    )


    data = [
        "Title: {title}",
        "----",
        "Subtitle: {subtitle}",
        "----",
        "Text: {text}",
        "----",
        "Categories: {category_list}",
        "----",
        "",
        "",
        "",
    ]








    def encode_to_filesystem( s ):
        result = s \
            .lower() \
            .replace( "å", "aa" ) \
            .replace( "ø", "o" ) \
            .replace( "æ", "ae" ) \
            .replace( ", ", "-" ) \
            .replace( " ", "-" ) \
            .replace( "/", "" ) \
            .replace( ".", "" ) \
            .replace( ",", "" ) \
            .replace( "--", "-" )

        return result

    def to_file_contents( name, content ):
        with open( name, 'w' ) as target:
            target.write( content )




    # collect all parents

    """ """

    parents = set()

    for e in entries:
        parents.update( e.categories )

    print parents, len(parents)

    assert( len( categories ) == len( parents ) )

    # enumerate parents from 1

    counted_parents = enumerate( parents, 1 )

    """ """


    # PARENTS (categories)

    for n,c in counted_parents:

        c.set_ordinal( n )

        category_folder_name = encode_to_filesystem(c.name)
        category_folder_template = "{category_number:02d}-{category_name}"
        enumerated_category_folder_name = category_folder_template.format(
            category_number=n,
            category_name=category_folder_name
        )

        if not os.path.exists( enumerated_category_folder_name ):
            os.makedirs( enumerated_category_folder_name )

            # create file with category description
            category_description_file = "{0}/{0}.txt".format(
                enumerated_category_folder_name,
                enumerated_category_folder_name
            )

            # category description template
            category_description_template = "\n".join([
                'Title: {0}',
                '----',
                'Priority: {1}',
                '----',
                'Text: {2}'
            ])

            if not os.path.exists( category_description_file ):
                to_file_contents(
                    category_description_file,
                    category_description_template.format(
                        c.name, # 0
                        c.priority, # 1
                        lorem_ipsum() # 2
                    )
                )


    # CHILDREN

    print "Number of children: ", len(entries)

    enumerated_entries = enumerate( entries, 1 )
    enumerated_entry_folder = \
        "{category_counter:02d}-{category_name}/{child_counter:02d}-{child_name}"

    enumerated_entry_file = \
        enumerated_entry_folder + "/{child_counter:02d}-{child_name}.{extension}"

    for n, e in enumerated_entries:

        print e

        for c in e.categories:

            enumerated_entry_folder_name = \
                enumerated_entry_folder.format(
                    category_counter=c.ordinal,
                    category_name=encode_to_filesystem(c.name),
                    child_counter=n,
                    child_name=encode_to_filesystem(e.title)
                )

            if not os.path.exists( enumerated_entry_folder_name ):
                os.makedirs( enumerated_entry_folder_name )

                to_file_contents(
                    enumerated_entry_file
                )



                # create child folder
                    #   {category_counter}-{category_name}/{child_counter}-{child_name}

                #for n in child_category_names:
                #    if not os.path.exists( enumerated_category_folder_name ):
                #        os.makedirs( enumerated_category_folder_name )








    # CHILDREN
    # create child folder
    #   {category_counter}-{category_name}/{child_counter}-{child_name}
    # create child contents
    #   {category_counter}-{category_name}/{child_counter}-{child_name}/{child_counter}-{child_name}.txt
    # create child images
    #   {category_counter}-{category_name}/{child_counter}-{child_name}/{child_counter}-{child_name}.main.png
    #   {category_counter}-{category_name}/{child_counter}-{child_name}/{child_counter}-{child_name}.thumb.png
    # create



    """



    with open("output.txt", "w") as output:


        data = '\n'.join( data )

        for e in entries:
            output.write(
                data.format(
                    title=e.title,
                    subtitle=e.title,
                    text=e.title,
                    category_list=", ".join( [c.name for c in e.categories] )
                )
            )

    # start recreating the file structure


    import os

    name_template = "{counter:02d}-{name}"


    for cn,c in enumerate(categories, 1):

        directory_name = name_template.format(
            name=c.get_filesystem_name(),
            counter=cn
        )

        if not os.path.exists( directory_name ):
            os.makedirs( directory_name )

            with open( "{c}/{c}.txt".format(c=directory_name), "w" ) as directory_descriptor:
                directory_descriptor.write(
                    "Name: {c}\n----\nPriority: {p}\n----\n".format(c=c.name, p=c.priority)
                )


        for en,e in enumerate(entries, 1):

            print c.name, c.name in [i.name for i in e.categories], [i.name for i in e.categories]

            if c.name in [i.name for i in e.categories]:

                from random import random
                category_hue = random()


                try:
                    file_name = "{counter:02d}-{name}".format( name=e.get_filesystem_title(), counter=en )
                    file_name_no_prefix = "{name}".format( name=e.get_filesystem_title() )

                    file_directory_name = "/".join([
                        name_template.format( name=c.get_filesystem_name(), counter=cn ),
                        file_name
                    ])



                    if not os.path.exists( file_directory_name ):
                        os.makedirs( file_directory_name )

                    # generate random placeholder image

                    import numpy, Image, colorsys



                    a = numpy.random.rand( 10, 10, 3 ) * 255


                    colors = []

                    for m in a:
                        buffer = []

                        for h,s,v in m:
                            buffer.append( colorsys.hsv_to_rgb( category_hue ,s,v ) )
                        colors.append( buffer )
                        buffer = []


                    a = numpy.array(colors)

                    im_out = Image.fromarray( a.astype('uint8') ).convert('RGBA')
                    im_out = im_out.resize( (305, 220), Image.NEAREST )
                    im_out.save( '{dn}/thumb.png'.format(dn=file_directory_name, fn=file_name_no_prefix ))
                    im_out = im_out.resize( ( 1024, 768 ), Image.NEAREST )
                    im_out.save( '{dn}/main.png'.format(dn=file_directory_name, fn=file_name_no_prefix ))

                    with open( "{dn}/{fn}.txt".format(dn=file_directory_name, fn=file_name ), "w" ) as target:

                        target.write(
                            data.format(
                                title=e.title,
                                subtitle=e.title,
                                text=e.title,
                                category_list=", ".join( [c.name for c in e.categories] )
                            )
                        )

                except OSError:
                    pass


        """