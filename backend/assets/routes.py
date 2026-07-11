from flask import render_template, redirect, url_for, flash, request
from backend.assets import assets_bp
from backend.assets.forms import AssetForm
from backend.extensions import db
from backend.models.asset import Asset


# ==========================
# View All Assets
# ==========================
@assets_bp.route("/")
def list_assets():

    search = request.args.get("search", "")

    if search:
        assets = Asset.query.filter(
            Asset.asset_name.contains(search)
        ).all()
    else:
        assets = Asset.query.order_by(
            Asset.id.desc()
        ).all()

    return render_template(
        "assets.html",
        assets=assets,
        search=search,
        active_page="assets"
    )


# ==========================
# Add Asset
# ==========================
@assets_bp.route("/add", methods=["GET", "POST"])
def add_asset():

    form = AssetForm()

    if form.validate_on_submit():

        asset = Asset(
            asset_name=form.asset_name.data,
            asset_code=form.asset_code.data,
            category=form.category.data,
            status=form.status.data,
            purchase_date=form.purchase_date.data
        )

        db.session.add(asset)
        db.session.commit()

        flash("Asset added successfully!", "success")

        return redirect(url_for("assets.list_assets"))

    return render_template(
        "asset_form.html",
        form=form,
        title="Add Asset"
    )


# ==========================
# Edit Asset
# ==========================
@assets_bp.route("/edit/<int:id>", methods=["GET", "POST"])
def edit_asset(id):

    asset = Asset.query.get_or_404(id)

    form = AssetForm(obj=asset)

    if form.validate_on_submit():

        asset.asset_name = form.asset_name.data
        asset.asset_code = form.asset_code.data
        asset.category = form.category.data
        asset.status = form.status.data
        asset.purchase_date = form.purchase_date.data

        db.session.commit()

        flash("Asset updated successfully!", "success")

        return redirect(url_for("assets.list_assets"))

    return render_template(
        "asset_form.html",
        form=form,
        title="Edit Asset"
    )


# ==========================
# Delete Asset
# ==========================
@assets_bp.route("/delete/<int:id>")
def delete_asset(id):

    asset = Asset.query.get_or_404(id)

    db.session.delete(asset)
    db.session.commit()

    flash("Asset deleted successfully!", "success")

    return redirect(url_for("assets.list_assets"))