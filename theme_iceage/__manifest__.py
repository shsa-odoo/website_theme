{
    "name": "Iceage Theme",
    "description": "= Iceage Theme",
    "category": "Theme/Website",
    "summary": "iceage",
    "sequence": 300,
    "version": "2.0.0",
    "depends": ["theme_common"],
    "data": [
        "data/generate_primary_template.xml",
        "data/ir_asset.xml",
        "views/images.xml",
        "views/customizations.xml",
        "views/new_page_template.xml",
    ],
    "images": [
        "static/description/iceage_description.jpg",
        "static/description/iceage_screenshot.jpg",
    ],
    "images_preview_theme": {
        "website.s_cover_default_image": "/theme_iceage/static/src/img/snippets/s_cover.jpg",
        "website.s_text_image_default_image": "/theme_iceage/static/src/img/snippets/s_text_image.jpg",
        "website.s_masonry_block_default_image_1": "/theme_iceage/static/src/img/snippets/s_masonry_block.jpg",
        "website.s_image_text_default_image": "/theme_iceage/static/src/img/snippets/s_image_text.jpg",
        "website.s_parallax_default_image": "/theme_iceage/static/src/img/snippets/s_parallax.jpg",
        "website.s_picture_default_image": "/theme_iceage/static/src/img/snippets/s_picture.jpg",
    },
    "configurator_snippets": {
        "homepage": ["s_cover"],
    },
    "new_page_templates": {
        "about": {
            "personal": ["s_call_to_action"],
        },
        "team": {
            "5": ["s_picture"],
        },
    },
    "license": "LGPL-3",
    "assets": {
        "website.assets_editor": [
            "theme_iceage/static/src/js/tour.js",
        ],
    }
}
