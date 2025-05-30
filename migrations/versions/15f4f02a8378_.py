"""empty message

Revision ID: 15f4f02a8378
Revises: 
Create Date: 2025-05-07 11:17:26.423388

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '15f4f02a8378'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('achievements',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('achievement_name', sa.String(length=80), nullable=False),
    sa.Column('description', sa.String(length=255), nullable=True),
    sa.Column('criteria', sa.String(length=255), nullable=False),
    sa.Column('badge_image_url', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('exercises',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('description', sa.String(length=255), nullable=True),
    sa.Column('category', sa.String(length=50), nullable=False),
    sa.Column('difficulty_level', sa.String(length=50), nullable=False),
    sa.Column('muscle_groups', sa.String(length=100), nullable=False),
    sa.Column('demonstration_video_url', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=80), nullable=False),
    sa.Column('password', sa.String(length=120), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('registraion_date', sa.DateTime(), nullable=False),
    sa.Column('account_status', sa.String(length=20), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.create_table('workouts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('description', sa.String(length=255), nullable=True),
    sa.Column('difficulty_level', sa.String(length=50), nullable=False),
    sa.Column('creator', sa.String(length=100), nullable=False),
    sa.Column('duration_minutes', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('goals',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('goal_type', sa.String(length=50), nullable=False),
    sa.Column('target_value', sa.Float(), nullable=False),
    sa.Column('current_value', sa.Float(), nullable=False),
    sa.Column('start_date', sa.DateTime(), nullable=False),
    sa.Column('target_date', sa.DateTime(), nullable=False),
    sa.Column('status', sa.String(length=20), nullable=False),
    sa.Column('progress', sa.Float(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('measurements',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('date', sa.DateTime(), nullable=False),
    sa.Column('measurement_type', sa.String(length=50), nullable=False),
    sa.Column('value', sa.Float(), nullable=False),
    sa.Column('notes', sa.String(length=255), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('nutrition_plans',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('meal_type', sa.String(length=50), nullable=False),
    sa.Column('food_items', sa.String(length=255), nullable=False),
    sa.Column('calories', sa.Float(), nullable=False),
    sa.Column('macronutrients', sa.String(length=100), nullable=False),
    sa.Column('micronutrients', sa.String(length=100), nullable=True),
    sa.Column('date_created', sa.DateTime(timezone=True), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user_achievements',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('achievement_id', sa.Integer(), nullable=False),
    sa.Column('date_achieved', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['achievement_id'], ['achievements.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user_profiles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('height_cm', sa.Float(), nullable=False),
    sa.Column('weight_kg', sa.Float(), nullable=False),
    sa.Column('age_years', sa.Integer(), nullable=False),
    sa.Column('fitness_level', sa.String(length=50), nullable=False),
    sa.Column('goals', sa.String(length=100), nullable=False),
    sa.Column('health_conditions', sa.String(length=200), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user_workouts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('workout_id', sa.Integer(), nullable=False),
    sa.Column('date_completed', sa.DateTime(), nullable=False),
    sa.Column('performance_rating', sa.Integer(), nullable=True),
    sa.Column('notes', sa.String(length=255), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.ForeignKeyConstraint(['workout_id'], ['workouts.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('workout_exercises',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('workout_id', sa.Integer(), nullable=False),
    sa.Column('exercise_id', sa.Integer(), nullable=False),
    sa.Column('sets', sa.Integer(), nullable=False),
    sa.Column('reps', sa.Integer(), nullable=False),
    sa.Column('duration_seconds', sa.Integer(), nullable=True),
    sa.Column('rest_time_seconds', sa.Integer(), nullable=True),
    sa.Column('order', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['exercise_id'], ['exercises.id'], ),
    sa.ForeignKeyConstraint(['workout_id'], ['workouts.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('workout_exercises')
    op.drop_table('user_workouts')
    op.drop_table('user_profiles')
    op.drop_table('user_achievements')
    op.drop_table('nutrition_plans')
    op.drop_table('measurements')
    op.drop_table('goals')
    op.drop_table('workouts')
    op.drop_table('users')
    op.drop_table('exercises')
    op.drop_table('achievements')
    # ### end Alembic commands ###
