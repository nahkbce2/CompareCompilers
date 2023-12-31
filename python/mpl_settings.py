# -*- coding: utf-8 -*-

import matplotlib as mpl


def set_plot_params(fontfamily='serif', fontstyle='normal', fontvariant='normal', fontweight='normal',
                    fontstretch='normal', fontsize=20, useTex='False'):
    # make ticks longer and thicker
    mpl.rcParams['hatch.linewidth'] = 0.1
    mpl.rcParams['xtick.major.size'] = 8
    mpl.rcParams['xtick.minor.size'] = 4
    mpl.rcParams['xtick.major.width'] = 2
    mpl.rcParams['xtick.minor.width'] = 2
    mpl.rcParams['ytick.major.size'] = 8
    mpl.rcParams['ytick.minor.size'] = 4
    mpl.rcParams['ytick.major.width'] = 2
    mpl.rcParams['ytick.minor.width'] = 2
    # make border thicker
    mpl.rcParams['axes.linewidth'] = 2
    # make plotted lines thicker
    mpl.rcParams['lines.linewidth'] = 2
    # make fonts bigger
    mpl.rcParams['xtick.labelsize'] = fontsize
    mpl.rcParams['ytick.labelsize'] = fontsize
    mpl.rcParams['legend.fontsize'] = fontsize
    mpl.rcParams['axes.titlesize'] = fontsize
    mpl.rcParams['axes.labelsize'] = fontsize
    # save figure settings
    mpl.rcParams['savefig.bbox'] = 'tight'
    # set font properties
    mpl.rcParams['font.family'] = fontfamily
    mpl.rcParams['font.style'] = fontstyle  # 'normal', 'italic','oblique'
    mpl.rcParams['font.variant'] = fontvariant  # 'normal', 'small-caps'
    # 'light', 'normal', 'medium', 'semibold', 'bold', 'heavy', 'black'
    mpl.rcParams['font.weight'] = fontweight
    # ‘ultra-condensed’, ‘extra-condensed’, ‘condensed’, ‘semi-condensed’, ‘normal’, ‘semi-expanded’,
    # ‘expanded’, ‘extra-expanded’, ‘ultra-expanded’
    mpl.rcParams['font.stretch'] = fontstretch
    mpl.rcParams[
        'font.size'] = fontsize  # ['xx-small', 'x-small', 'small', 'medium', 'large','x-large', 'xx-large']
    mpl.rcParams['font.serif'] = ['Times', 'Times New Roman', 'Palatino', 'Bitstream Vera Serif',
                                  'New Century Schoolbook', 'Century Schoolbook L', 'Utopia', 'ITC Bookman',
                                  'Bookman', 'Nimbus Roman No9 L', 'Charter', 'serif']
    mpl.rcParams['font.sans-serif'] = ['Bitstream Vera Sans', 'Lucida Grande', 'Verdana', 'Geneva', 'Lucid',
                                       'Arial', 'Helvetica', 'Avant Garde', 'sans-serif']
    mpl.rcParams['font.cursive'] = ['Apple Chancery', 'Textile', 'Zapf Chancery', 'Sand', 'cursive']
    mpl.rcParams['font.fantasy'] = ['Comic Sans MS', 'Chicago', 'Charcoal', 'Impact', 'Western', 'fantasy']
    mpl.rcParams['font.monospace'] = ['Bitstream Vera Sans Mono', 'Andale Mono', 'Nimbus Mono L',
                                      'Courier New', 'Courier', 'Fixed', 'Terminal', 'monospace']
    mpl.rcParams['text.usetex'] = useTex
    # set math mode font properties
    mpl.rcParams['mathtext.cal'] = 'cursive'
    mpl.rcParams['mathtext.rm'] = 'serif'
    mpl.rcParams['mathtext.tt'] = 'monospace'
    mpl.rcParams['mathtext.it'] = 'serif:italic'
    mpl.rcParams['mathtext.bf'] = 'serif:bold'
    mpl.rcParams['mathtext.sf'] = 'sans'
    mpl.rcParams['mathtext.fontset'] = 'cm'  # Should be 'cm' (Computer Modern), 'stix','stixsans' or 'custom'
    mpl.rcParams['mathtext.fallback_to_cm'] = 'True'  # When True, use symbols from the Computer Modern fonts
    # when a symbol can not be found in one of the custom math fonts.

    mpl.rcParams['mathtext.default'] = 'rm'  # The default font to use for math. Can be any of the LaTeX font
    # names, including the special name "regular" for the same font used in regular text.
    mpl.rcParams['pdf.fonttype'] = 42  # Force matplotlib to use Type42 (a.k.a. TrueType) fonts for .pdf
    mpl.rcParams['ps.fonttype'] = 42  # Force matplotlib to use Type42 (a.k.a. TrueType) fonts for .eps

plot_params = dict()
plot_params['goldenRatio'] = 1.61803398875
plot_params['fhgt'] = 10.0
plot_params['fwid'] = plot_params['fhgt']*plot_params['goldenRatio']
plot_params['dpi'] = 300

plot_params['AnnotateXXLarge'] = 72
plot_params['AnnotateXLarge'] = 48
plot_params['AnnotateLarge'] = 32
plot_params['AnnotateMedium'] = 28
plot_params['AnnotateSmall'] = 24
plot_params['AnnotateXSmall'] = 20
plot_params['AnnotateXXSmall'] = 16

plot_params['LegendLarge'] = 24
plot_params['LegendMedium'] = 20
plot_params['LegendSmall'] = 16
plot_params['LegendXSmall'] = 12
plot_params['LegendXXSmall'] = 10
plot_params['LegendXXXSmall'] = 8

plot_params['LabelXLarge'] = 32
plot_params['LabelLarge'] = 28
plot_params['LabelMedium'] = 24
plot_params['LabelSmall'] = 20
plot_params['LabelXSmall'] = 16

plot_params['AxisXXLarge'] = 32
plot_params['AxisXLarge'] = 28
plot_params['AxisLarge'] = 24
plot_params['AxisMedium'] = 20
plot_params['AxisSmall'] = 16
plot_params['AxisXSmall'] = 12
plot_params['AxisXXSmall'] = 8

plot_params['normalFontSize'] = 32
plot_params['smallFontSize'] = 24
plot_params['footnoteFontSize'] = 20
plot_params['scriptFontSize'] = 16
plot_params['tinyFontSize'] = 12
