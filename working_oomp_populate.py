"""Editable KALLAX documentation recipe. All dimensions are millimetres."""
import copy

CONFIGURATION_ID = "project_github_oomlout_three_d_printing_filament_storage_kallax_one_cell"

def define_project_readme(**kwargs):
    kwargs = copy.deepcopy(kwargs)
    kwargs.setdefault("title", "KALLAX filament holders")
    kwargs.setdefault("summary", "3D-printable holders for storing 3D printer filament in an IKEA KALLAX shelving unit. One cell holds five reels at the front and five strapped filament refills without spools on a raised rear row. This repository includes printable files, editable source and illustrated assembly instructions.")
    kwargs.setdefault("ai_notice", "This is an entirely AI-generated coding project. The source code is largely unreadable by humans, but usable generated files are included. It is published so others can use their own AI tools to understand, modify and regenerate the design.")
    kwargs.setdefault("credit", None)  # No external design inspiration was established in the source record.
    kwargs.setdefault("viewer_url", None)  # Set only after a real hosted HTML endpoint is published and checked.
    kwargs.setdefault("version_title", "One cell")
    kwargs.setdefault("version_description", "Four short and four tall frames; four adjustable M6 rails. Five front reels and five rear refills.")
    kwargs.setdefault("installation", "Place the tall holder at the rear and the short holder at the front. Seat all feet on the shelf. Load the strapped rear refills, then the five front reels.")
    return kwargs

def define_assembly_book(**kwargs):
    kwargs = copy.deepcopy(kwargs)
    kwargs.setdefault("cover_title", "KALLAX filament holders")
    kwargs.setdefault("cover_subtitle", "One cell / short and tall holders / M6 adjustable rails")
    kwargs.setdefault("project_name", "three_d_printing_filament_storage_kallax_holder")
    kwargs.setdefault("project_url", "https://github.com/oomlout/three_d_printing_filament_storage_kallax_holder")
    kwargs.setdefault("viewer_enabled", True)
    kwargs.setdefault("viewer_start", "page-03")
    kwargs.setdefault("viewer_layout", "a4-landscape-four-step")
    kwargs.setdefault("logo_svg", "source_file/oomlout_logo_unshaded_original.svg")
    kwargs.setdefault("logo_symbol_subpaths", 3)
    kwargs.setdefault("details_title", "Project details")
    kwargs.setdefault("details", [
        "One cell: independent short front holder and tall rear holder. Four frames and two rails per holder.",
        "Nominal opening: 335 mm. Rail heights: 37 mm front, 112 mm rear. Row centres: 187 mm.",
        "Print all plastic parts in black. Use the 7 mm nut covers and 7 mm slotted covers.",
        "Cut four M6 threaded rods to 300 mm and deburr the ends. Prepare a 10 mm spanner.",
        "Each rail: one 18 mm M6 coupling nut, one M6 x 25 fully threaded hex bolt and two M6 nuts.",
        "Seat the fixed nut and bolt head in the outer frame recesses. Retain the bolt with an inner nut.",
        "Nominal coupling engagement: rod 5.99 mm; bolt 7 mm. Bolt length is measured under the head.",
        "Measure the actual opening before adjustment. Do not force the cabinet sides apart.",
        "Keep refills strapped. Illustrated front reels are 200 mm diameter x 60 mm wide.",
        "M6 x 300 threaded rod: OOMP record pending. No shortlink is assigned.",
        "AI-generated CAD images and instructions. Errors possible. Physical fit and load capacity untested.",
    ])
    kwargs.setdefault("summary_title", "Printed parts")
    kwargs.setdefault("hardware_title", "Hardware")
    kwargs.setdefault("summary_step", True)
    kwargs.setdefault("summary_view", "book_cover")
    kwargs.setdefault("signature_pages", 4)
    return kwargs

def define_assembly_cards(**kwargs):
    """Repeat the complete six-operation sequence; the front holder persists in rear views."""
    cards = []
    for row, frame in [("front", "short"), ("rear", "tall")]:
        prefix = row + "_"
        recipe = [
            {
                "title": "Start the " + frame + " holder",
                "action": "Seat two M6 nuts in the first " + frame + " frame's outer recesses. Thread in two 300 mm rods with their ends flush with the nuts.",
                "add": ["frame_1", "fixed_*", "rod_*"],
                "move": {"fixed_*": [-18, 0, 0], "rod_*": [18, 0, 0]},
            },
            {
                "title": "Fit the first sleeves",
                "action": "Slide one 99.67 mm sleeve onto each rod, then fit the second frame.",
                "add": ["long_first_*", "frame_2"],
                "move": {"long_first_*": [20, 0, 0], "frame_2": [40, 0, 0]},
            },
            {
                "title": "Fit the centre and remaining sleeves",
                "action": "Fit two 67.67 mm sleeves, the third frame and two 99.67 mm sleeves. Face the last sleeves' hex pockets toward the couplings.",
                "add": ["centre_*", "frame_3", "long_last_*"],
                "move": {"centre_*": [20, 0, 0], "frame_3": [40, 0, 0], "long_last_*": [60, 0, 0]},
            },
            {
                "title": "Fit the couplings",
                "action": "Insert an M6 coupling nut into each 18 mm housing. Thread each coupling approximately 6 mm onto its rod.",
                "add": ["coupling_*", "housing_*"],
                "move": {"coupling_*": [25, 0, 0], "housing_*": [50, 0, 0]},
            },
            {
                "title": "Fit the adjusting end",
                "action": "Face the final frame's recesses outward. Insert the M6 x 25 hex bolts, add retaining nuts loosely and slide the 7 mm hex covers over them. Thread the bolt tips into the couplings.",
                "add": ["frame_4", "bolt_*", "retaining_*", "nut_cover_*"],
                "move": {"nut_cover_*": [20, 0, 0], "retaining_*": [35, 0, 0], "frame_4": [50, 0, 0], "bolt_*": [70, 0, 0]},
            },
            {
                "title": "Adjust and close the rails",
                "action": "Set the width to the measured opening, nominally 335 mm. Seat the bolt heads in the outer recesses. Slide the hex covers aside, tighten the retaining nuts against the inner frame face, then replace the covers. Clip the 7 mm slotted covers over the exposed thread, slots downward.",
                "add": ["clip_*"],
                "move": {"clip_*": [0, 0, 22]},
            },
        ]
        for step in recipe:
            step["add"] = [prefix + p for p in step["add"]]
            step["move"] = {prefix + p: v for p, v in step["move"].items()}
            cards.append(step)
    return copy.deepcopy(cards)

def define(**kwargs):
    kwargs = copy.deepcopy(kwargs)
    kwargs.setdefault("id", CONFIGURATION_ID)
    kwargs.setdefault("parts", define_assembly_part_labels())
    kwargs.setdefault("style", define_assembly_card_style())
    kwargs.setdefault("book", define_assembly_book())
    kwargs.setdefault("steps", define_assembly_cards())
    kwargs.setdefault("readme", define_project_readme())
    return kwargs

def define_assembly_part_labels(**kwargs):
    kwargs = copy.deepcopy(kwargs)
    kwargs.setdefault("parts", PARTS)
    return copy.deepcopy(kwargs["parts"])

def define_assembly_card_style(**kwargs):
    """Four largely pictorial panels on landscape A4; dimensions in mm."""
    kwargs = copy.deepcopy(kwargs)
    kwargs.setdefault("page_mm", [297, 210])
    kwargs.setdefault("columns", 2)
    kwargs.setdefault("rows", 2)
    kwargs.setdefault("margin_mm", 6)
    kwargs.setdefault("gutter_mm", 4)
    kwargs.setdefault("border_radius_mm", 3)
    kwargs.setdefault("border_width_pt", 3.0)
    kwargs.setdefault("component_border_width_pt", 1.1)
    kwargs.setdefault("thumbnail_height_mm", 8.5)
    kwargs.setdefault("quantity_shift_mm", 1.0)
    kwargs.setdefault("paper", "FFFFFF")
    kwargs.setdefault("ink", "000000")
    kwargs.setdefault("accent", "000000")
    kwargs.setdefault("border", "000000")
    kwargs.setdefault("image_size", [1500, 1100])
    kwargs.setdefault("samples", 24)
    kwargs.setdefault("eye", [1.2, -1.6, 1.35])
    kwargs.setdefault("underside_eye", [1.2, -1.6, -1.5])
    kwargs.setdefault("font_body_pt", 7)
    kwargs.setdefault("font_code_pt", 6.4)
    kwargs.setdefault("font_url_prefix_pt", 4.8)
    kwargs.setdefault("quantity_pt", 5.8)
    kwargs.setdefault("explosion_scale", 1.35)
    kwargs.setdefault("draw_arrows", False)
    kwargs.setdefault("revision", "4")
    kwargs.setdefault("title", "KALLAX filament holders")
    return kwargs


PARTS = {'P1': {'name': 'Short side frame',
        'detail': '149 x 44 x 9 mm',
        'id': 'project_github_oomlout_three_d_printing_filament_storage_kallax_side_10_width_3_height_9_mm_depth_short_extra',
        'stl': 'parts/project_github_oomlout_three_d_printing_filament_storage_kallax_side_10_width_3_height_9_mm_depth_short_extra/3dpr.stl',
        'printed': True,
        'quantity': 4},
 'P2': {'name': 'Tall side frame',
        'detail': '149 x 119 x 9 mm',
        'id': 'project_github_oomlout_three_d_printing_filament_storage_kallax_side_10_width_8_height_9_mm_depth_short_extra',
        'stl': 'parts/project_github_oomlout_three_d_printing_filament_storage_kallax_side_10_width_8_height_9_mm_depth_short_extra/3dpr.stl',
        'printed': True,
        'quantity': 4},
 'P3': {'name': 'Sleeve 99.67 mm',
        'detail': '99.67 mm long; one-end hex pocket',
        'id': 'project_github_oomlout_three_d_printing_filament_storage_kallax_spacer_1_width_1_height_99_67_mm_depth_one_end_nut_extra',
        'stl': 'parts/project_github_oomlout_three_d_printing_filament_storage_kallax_spacer_1_width_1_height_99_67_mm_depth_one_end_nut_extra/3dpr.stl',
        'printed': True,
        'quantity': 8},
 'P4': {'name': 'Sleeve 67.67 mm',
        'detail': '67.67 mm long; one-end hex pocket',
        'id': 'project_github_oomlout_three_d_printing_filament_storage_kallax_spacer_1_width_1_height_67_67_mm_depth_one_end_nut_extra',
        'stl': 'parts/project_github_oomlout_three_d_printing_filament_storage_kallax_spacer_1_width_1_height_67_67_mm_depth_one_end_nut_extra/3dpr.stl',
        'printed': True,
        'quantity': 4},
 'P5': {'name': 'Coupling housing 18 mm',
        'detail': '18 mm long; full hex bore',
        'id': 'project_github_oomlout_three_d_printing_filament_storage_kallax_spacer_1_width_1_height_18_mm_depth_full_nut_extra',
        'stl': 'parts/project_github_oomlout_three_d_printing_filament_storage_kallax_spacer_1_width_1_height_18_mm_depth_full_nut_extra/3dpr.stl',
        'printed': True,
        'quantity': 4},
 'P6': {'name': 'Nut cover 7 mm',
        'detail': '7 mm long; full hex bore',
        'id': 'project_github_oomlout_three_d_printing_filament_storage_kallax_spacer_1_width_1_height_7_mm_depth_full_nut_extra',
        'stl': 'parts/project_github_oomlout_three_d_printing_filament_storage_kallax_spacer_1_width_1_height_7_mm_depth_full_nut_extra/3dpr.stl',
        'printed': True,
        'quantity': 4},
 'P7': {'name': 'Slotted cover 7 mm',
        'detail': '7 mm long; open slot',
        'id': 'project_github_oomlout_three_d_printing_filament_storage_kallax_spacer_1_width_1_height_7_mm_depth_slotted_extra',
        'stl': 'parts/project_github_oomlout_three_d_printing_filament_storage_kallax_spacer_1_width_1_height_7_mm_depth_slotted_extra/3dpr.stl',
        'printed': True,
        'quantity': 4},
 'H1': {'name': 'M6 x 300 threaded rod',
        'detail': '300 mm cut length; M6 x 1.0',
        'id': 'project_local_m6_threaded_rod_300_mm',
        'quantity': 4,
        'catalogue_status': 'pending',
        'identity_source': 'User requested OOMP record pending on 2026-11-07; no supplier link in '
                           'README.'},
 'H2': {'name': 'M6 hex nut',
        'detail': '10 mm AF; 5 mm nominal thickness',
        'id': 'hardware_nut_m6',
        'quantity': 8,
        'catalogue_status': 'verified',
        'identity_source': 'OOMP identity verified 2026-11-06; actual thickness to be checked',
        'md5_6_alpha': 'hcps',
        'short_url': 'https://oom.lt/a/hcps',
        'url': 'https://github.com/oomlout/oomp_hardware_bolt_version_5/tree/main/parts/hardware_nut_m6'},
 'H3': {'name': 'M6 coupling nut 18 mm',
        'detail': 'DIN 6334; 18 mm long; 10 mm AF',
        'id': 'hardware_nut_m6_coupling',
        'quantity': 4,
        'catalogue_status': 'verified',
        'identity_source': 'OOMP identity verified 2026-11-06; 18 mm dimensions from Accu',
        'md5_6_alpha': '1qsz8',
        'short_url': 'https://oom.lt/a/1qsz8',
        'url': 'https://github.com/oomlout/oomp_hardware_bolt_version_5/tree/main/parts/hardware_nut_m6_coupling'},
 'H4': {'name': 'M6 x 25 hex bolt',
        'detail': '25 mm under head; M6 x 1.0; DIN 933',
        'id': 'hardware_set_screw_m6_25_mm_length',
        'quantity': 4,
        'catalogue_status': 'verified',
        'identity_source': 'OOMP full-thread hex-head identity verified 2026-11-06; no grub screw',
        'md5_6_alpha': '9dg7e',
        'short_url': 'https://oom.lt/a/9dg7e',
        'url': 'https://github.com/oomlout/oomp_hardware_bolt_version_5/tree/main/parts/hardware_set_screw_m6_25_mm_length'}}
